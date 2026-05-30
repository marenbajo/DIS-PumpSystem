import customtkinter as ctk
from tkinter import messagebox
from app.config import TEXT_STYLE, COMBO_STYLE
from components.step_frame import StepFrame
from components.reco_frame import RecoFrame
from data.pdf_exporter import export_session_to_pdf


class StepRecoTab(ctk.CTkFrame):
    def __init__(self, master, folder_path, test_number, date_value, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        # Store session info
        self.folder_path = folder_path
        self.test_number = test_number
        self.date_value = date_value

        # Counters
        self.step_count = 1
        self.reco_count = 0

        # Layout
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        # Dictionary of frames
        self.frames = {}

        # --- ComboBox for tab selection ---
        self.tab_selector = ctk.CTkComboBox(
            self,
            values=["Step 1"],
            command=self.show_tab,
            width=150,
            **COMBO_STYLE
        )
        self.tab_selector.grid(row=0, column=0, pady=(8, 6), sticky="n")

        # --- Content container ---
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.grid(row=1, column=0, sticky="nsew")
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        # First tab
        self.add_step_tab(initial=True)

    # --- Tab creation --------------------------------------------------------
    def _next_step_number(self):
        existing_steps = [
            int(name.split()[1])
            for name in self.frames.keys()
            if name.startswith("Step")
        ]
        n = 2
        while n in existing_steps:
            n += 1
        return n

    def add_step_tab(self, initial=False):
        if initial:
            tab_name = "Step 1"
        else:
            self.step_count = self._next_step_number()
            tab_name = f"Step {self.step_count}"

        values = list(self.frames.keys()) + [tab_name]
        self.tab_selector.configure(values=values)
        self.tab_selector.set(tab_name)

        frame = StepFrame(
            self.container,
            tabview=self,
            step_name=tab_name,
            folder_path=self.folder_path,
            test_number=self.test_number,
            date_value=self.date_value
        )
        frame.grid(row=0, column=0, sticky="nsew")
        self.frames[tab_name] = frame

        self.show_tab(tab_name)

    def add_reco_tab(self):
        self.reco_count += 1
        tab_name = f"Recovery {self.reco_count}"

        values = list(self.frames.keys()) + [tab_name]
        self.tab_selector.configure(values=values)
        self.tab_selector.set(tab_name)

        frame = RecoFrame(
            self.container,
            tabview=self,
            reco_name=tab_name,
            folder_path=self.folder_path,
            test_number=self.test_number,
            date_value=self.date_value
        )
        frame.grid(row=0, column=0, sticky="nsew")
        self.frames[tab_name] = frame

        self.show_tab(tab_name)

    # --- Tab switching -------------------------------------------------------
    def show_tab(self, tab_name):
        frame = self.frames.get(tab_name)
        if frame:
            frame.tkraise()

    # --- Tab closing ---------------------------------------------------------
    def close_current_tab(self):
        current_tab = self.tab_selector.get()
        if not current_tab:
            return

        if current_tab == "Step 1":
            messagebox.showinfo("Protected Tab", "Step 1 cannot be closed.")
            return

        answer = messagebox.askyesno("Confirm Close", f"Are you sure you want to close '{current_tab}'?")
        if not answer:
            return

        frame = self.frames.pop(current_tab, None)
        if frame:
            frame.destroy()

        values = list(self.frames.keys())
        self.tab_selector.configure(values=values)
        if values:
            self.tab_selector.set(values[0])
            self.show_tab(values[0])

    # --- Save current tab ----------------------------------------------------
    def save_current_tab(self):
        current_tab = self.tab_selector.get()
        if not current_tab:
            return

        frame = self.frames.get(current_tab)
        if frame and hasattr(frame, "save_data"):
            frame.save_data()
        else:
            messagebox.showinfo("Save", f"No saveable frame found in '{current_tab}'")

    # --- Finish session (EXPORT PDF) ----------------------------------------
    def finish_session(self):
        pdf_path = export_session_to_pdf(
            self.folder_path,
            self.test_number,
            self.date_value
        )
        messagebox.showinfo("PDF Exported", f"PDF saved to:\n{pdf_path}")
