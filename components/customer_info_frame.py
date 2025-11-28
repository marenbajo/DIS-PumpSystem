# components/info_frame.py
import customtkinter as ctk
import datetime
from data.save_file import start_new_session, save_customer_info
from components.notes_frame import NotesFrame
from app.config import TEXT_STYLE, BUTTON_STYLE

class InfoFrame(ctk.CTkFrame):
    def __init__(self, master, autosave_interval=60000, status_label=None, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.entries = {}
        self.autosave_interval = autosave_interval

        # Create session folder when InfoFrame starts
        self.folder_path, self.test_number, self.date_value = start_new_session()

        # Shared status label (passed in from App)
        self.status_label = status_label

        # Layout grid
        for r in range(5):
            self.grid_rowconfigure(r, weight=1, uniform="row")
        for c in range(6):
            self.grid_columnconfigure(c, weight=1, uniform="column")

        # Field groups
        fields_l = ["Client Name: ", "Farm Name: ", "Borehole depth: ", "Latitude (ºS): "]
        fields_c = ["Date: ", "Borehole Number: ", "Borehole size: ", "Longitude (ºE): "]
        fields_r = ["Time: ", "Borehole location/Name: ", "Collar height\n(Level before pumping):", "Elevation: "]

        for r, field in enumerate(fields_l):
            self.add_field(r, 0, field)
        for r, field in enumerate(fields_c):
            self.add_field(r, 2, field)
        for r, field in enumerate(fields_r):
            self.add_field(r, 4, field)

        # Pre-fill date and time
        now = datetime.datetime.now()
        if "Date:" in self.entries:
            self.entries["Date:"].insert(0, now.strftime("%Y-%m-%d"))
        if "Time:" in self.entries:
            self.entries["Time:"].insert(0, now.strftime("%H:%M"))

        # Notes section
        self.notes_frame = NotesFrame(self)
        self.notes_frame.grid(row=4, column=0, rowspan=2, columnspan=6,
                              padx=10, pady=(10, 0), sticky="sew")

        # Save button
        self.save_button = ctk.CTkButton(
            self,
            text="Save Customer Info",
            command=self.save_data,
            **BUTTON_STYLE
        )
        self.save_button.grid(row=6, column=0, columnspan=6,
                              pady=(10, 10), padx=10, sticky="e")

        # If no shared status label was passed, create a local one
        if not self.status_label:
            self.status_label = ctk.CTkLabel(self, text="", font=("Times New Roman", 12))
            self.status_label.grid(row=7, column=0, columnspan=6, pady=(5, 5), sticky="w")

        # Autosave
        self.schedule_autosave()

    def add_field(self, row, col, text):
        label = ctk.CTkLabel(self, text=text, **TEXT_STYLE, anchor="e")
        label.grid(row=row, column=col, padx=(10, 5), pady=5, sticky="w")

        entry = ctk.CTkEntry(
            self,
            placeholder_text=f"Enter {text.replace(':', '').replace('\n', ' ')}",
            **TEXT_STYLE
        )
        entry.grid(row=row, column=col + 1, padx=(5, 10), pady=5, sticky="w")

        self.entries[text.strip()] = entry

    def collect_data(self):
        data = {field: entry.get() for field, entry in self.entries.items()}
        notes = ""
        if hasattr(self.notes_frame, "textbox"):
            notes = self.notes_frame.textbox.get("1.0", "end").strip()
        elif hasattr(self.notes_frame, "get"):
            notes = self.notes_frame.get().strip()
        return data, notes

    def save_data(self):
        info_data, notes = self.collect_data()
        filename = save_customer_info(
            info_data,
            notes,
            self.folder_path,
            self.test_number,
            self.date_value
        )
        now = datetime.datetime.now()
        if self.status_label:
            self.status_label.configure(
                text=f"Saved Customer Info for Test {self.test_number} at {now.strftime('%Y-%m-%d %H:%M')}"
            )
        print(f"[Manual/Auto Save] Customer info updated in {filename}")

    def schedule_autosave(self):
        self.save_data()
        self.after(self.autosave_interval, self.schedule_autosave)
