import csv
import os
import sys
from fpdf import FPDF
from paths import get_data_dir

def _resource_path(filename):
    """Gibt den Pfad zu einer Ressource im data/-Ordner zurück."""
    return os.path.join(get_data_dir(), filename)

# Brand colors (R, G, B)
BLUE       = (22, 73, 196)    # #1649C4
DARK_BLUE  = (29, 29, 89)     # #1D1D59
LIGHT_BLUE = (192, 203, 254)  # #C0CBFE
WHITE      = (255, 255, 255)
BLACK      = (0, 0, 0)
LIGHT_GRAY = (245, 245, 245)
BORDER_COLOR = (180, 180, 200)

PAGE_W    = 210   # A4 width mm
MARGIN    = 15
CONTENT_W = PAGE_W - 2 * MARGIN  # 180mm

# Logo: 1024x187px → scaled to full content width (180mm), height proportional
LOGO_W    = CONTENT_W          # 180mm
LOGO_H    = round(LOGO_W * 187 / 1024, 1)  # ~32.9mm
BANNER_H  = LOGO_H + 4        # small padding below logo

LOGO_PATH = _resource_path("dis_logo.jpg")


class ReportPDF(FPDF):
    def __init__(self, test_number, date_value):
        super().__init__()
        self.test_number = test_number
        self.date_value  = date_value
        # top margin leaves room for logo + test info line
        self.set_margins(MARGIN, BANNER_H + 12, MARGIN)
        self.set_auto_page_break(auto=True, margin=MARGIN)

    def header(self):
        # Logo – full content width, left-aligned at margin
        if os.path.exists(LOGO_PATH):
            self.image(LOGO_PATH, x=MARGIN, y=4, w=LOGO_W)

        # Test number + date line underneath the logo
        info_y = 4 + LOGO_H + 1
        self.set_xy(MARGIN, info_y)
        self.set_font("Arial", "", 10)
        self.set_text_color(*DARK_BLUE)
        self.cell(CONTENT_W / 2, 6,
                  f"Test Nr. {self.test_number}  |  {self.date_value}",
                  border=0, align="L")
        self.set_text_color(*BLACK)
        # Position cursor below banner for content
        self.set_y(BANNER_H + 12)

    def footer(self):
        self.set_y(-12)
        self.set_font("Arial", "I", 8)
        self.set_text_color(*BLACK)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    # ------------------------------------------------------------------
    # Section label (matches the wireframe boxes)
    # ------------------------------------------------------------------
    def section_label(self, title):
        self.ln(3)
        self.set_fill_color(*WHITE)
        self.set_draw_color(*BLACK)
        self.set_font("Arial", "B", 11)
        self.set_text_color(*BLACK)
        self.cell(CONTENT_W, 8, f"  {title}", border=1, fill=False, ln=1)

    # ------------------------------------------------------------------
    # Customer info (2-column key:value grid)
    # ------------------------------------------------------------------
    def customer_info_section(self, rows):
        self.section_label("Customer Information")
        self.ln(2)

        # Keep only real data rows, drop metadata
        skip = {"Customer_Information", "Timestamp", "TestNumber", "Notes"}
        data = [(r[0].rstrip(":").strip().replace("\n", " "), r[1]) for r in rows
                if len(r) == 2 and r[0].strip() not in skip]

        label_w = 80
        val_w   = CONTENT_W - label_w

        for key, val in data:
            self.set_font("Arial", "B", 10)
            self.cell(label_w, 7, key + ":", border=0)
            self.set_font("Arial", "", 10)
            self.cell(val_w, 7, val, border=0)
            self.ln(7)

        # Notes
        notes_row = next((r for r in rows
                          if len(r) == 2 and r[0].strip() == "Notes"), None)
        if notes_row and notes_row[1].strip():
            self.ln(2)
            self.set_font("Arial", "B", 10)
            self.cell(CONTENT_W, 6, "Notes:", ln=1)
            self.set_font("Arial", "", 10)
            self.multi_cell(CONTENT_W, 5, notes_row[1].strip())

        self.ln(4)

    # ------------------------------------------------------------------
    # Generic table
    # ------------------------------------------------------------------
    def data_table(self, headers, rows, col_widths):
        # Table header row – bold, black border, no fill
        self.set_draw_color(*BLACK)
        self.set_font("Arial", "B", 9)
        self.set_text_color(*BLACK)
        for header, w in zip(headers, col_widths):
            self.cell(w, 7, header, border=1, fill=False, align="C")
        self.ln()

        # Data rows – no fill, black border
        self.set_font("Arial", "", 9)
        for row in rows:
            for cell_val, w in zip(row, col_widths):
                self.cell(w, 6, str(cell_val) if cell_val else "",
                          border=1, fill=False, align="C")
            self.ln()

        self.ln(4)


# ------------------------------------------------------------------
# CSV parsing helpers
# ------------------------------------------------------------------

def _parse_steps(csv_path):
    """Return (ordered list of step names, dict step_name -> list of data rows).
    Each data row: [time, waterlevel, meter, calc_meter, q]
    """
    steps  = {}
    order  = []
    current = None

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header line
        for row in reader:
            if not row:
                continue
            label = row[0].strip()
            if label.startswith("Step"):
                current = label
                steps[current] = []
                order.append(current)
            if current is not None and len(row) >= 6:
                # row: [step_label, time, wl, meter, calc, q]
                data_row = row[1:6]   # time, wl, meter, calc, q
                steps[current].append(data_row)

    return order, steps


def _parse_recoveries(csv_path):
    """Return (ordered list of reco names, dict reco_name -> list of data rows).
    Each data row: [time, waterlevel, s]
    """
    recoveries = {}
    order      = []
    current    = None

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header line
        for row in reader:
            if not row:
                continue
            label = row[0].strip()
            if label.startswith("Recovery"):
                current = label
                recoveries[current] = []
                order.append(current)
            if current is not None and len(row) >= 3:
                # row: [reco_label, time, wl, s]
                data_row = row[1:4]   # time, wl, s
                recoveries[current].append(data_row)

    return order, recoveries


# ------------------------------------------------------------------
# Main export function
# ------------------------------------------------------------------

def export_session_to_pdf(session_folder, test_number, date_value):
    """Read all CSVs in session_folder and produce a structured PDF on the Desktop."""

    desktop    = os.path.join(os.path.expanduser("~"), "Desktop")
    pdf_path   = os.path.join(desktop, f"Pump_Test_Report_{test_number}_{date_value}.pdf")

    pdf = ReportPDF(test_number, date_value)
    pdf.add_page()

    # 1. Customer Information
    customer_file = next(
        (os.path.join(session_folder, f) for f in os.listdir(session_folder)
         if f.startswith("Customer_Information") and f.endswith(".csv")),
        None
    )
    if customer_file:
        with open(customer_file, "r", encoding="utf-8") as fh:
            rows = list(csv.reader(fh))
        pdf.customer_info_section(rows)

    # 2. Steps
    steps_file = next(
        (os.path.join(session_folder, f) for f in os.listdir(session_folder)
         if f.startswith("Steps_") and f.endswith(".csv")),
        None
    )
    if steps_file:
        step_order, steps = _parse_steps(steps_file)
        step_headers = ["Time (min)", "Waterlevel (m)", "Meter reading",
                        "Calc. Meter reading", "Q (m³/h)"]
        # 22 + 35 + 40 + 53 + 30 = 180
        step_widths  = [22, 35, 40, 53, 30]
        for name in step_order:
            pdf.section_label(name)
            pdf.data_table(step_headers, steps[name], step_widths)

    # 3. Recoveries
    reco_file = next(
        (os.path.join(session_folder, f) for f in os.listdir(session_folder)
         if f.startswith("Recovery_") and f.endswith(".csv")),
        None
    )
    if reco_file:
        reco_order, recoveries = _parse_recoveries(reco_file)
        reco_headers = ["Time (min)", "Waterlevel (m)", "s"]
        # 30 + 75 + 75 = 180
        reco_widths  = [30, 75, 75]
        for name in reco_order:
            pdf.section_label(name)
            pdf.data_table(reco_headers, recoveries[name], reco_widths)

    pdf.output(pdf_path)
    return pdf_path
