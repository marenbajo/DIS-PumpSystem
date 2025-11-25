import customtkinter as ctk
from tkinter import messagebox
from app.config import TEXT_STYLE, SEGMENTED_STYLE
from components.step_frame import StepFrame
from components.reco_frame import RecoFrame

class StepRecoTab(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        # Style segmented button
        self._segmented_button.configure(**TEXT_STYLE, **SEGMENTED_STYLE)

        # Counters
        self.step_count = 1
        self.reco_count = 0

        # Expand tabview
        self.rowconfigure(0, weight=0)
        self.columnconfigure(0, weight=1)

        # First tab (Step 1)
        self.add("Step 1")
        self.set("Step 1")

        tab_content = self.tab("Step 1")
        tab_content.grid_rowconfigure(0, weight=1)
        tab_content.grid_columnconfigure(0, weight=1)

        step_frame = StepFrame(tab_content, tabview=self)
        step_frame.grid(row=0, column=0, sticky="nsew")

    def _next_step_number(self):
        existing_steps = [
            int(name.split()[1])
            for name in self._name_list
            if name.startswith("Step")
        ]
        n = 2
        while n in existing_steps:
            n += 1
        return n

    def add_step_tab(self):
        self.step_count = self._next_step_number()
        tab_name = f"Step {self.step_count}"
        self.add(tab_name)
        self.set(tab_name)

        tab_content = self.tab(tab_name)
        tab_content.grid_rowconfigure(0, weight=1)
        tab_content.grid_columnconfigure(0, weight=1)

        step_frame = StepFrame(tab_content, tabview=self)
        step_frame.grid(row=0, column=0, sticky="nsew")

    def add_reco_tab(self):
        self.reco_count += 1
        tab_name = f"Recovery {self.reco_count}"
        self.add(tab_name)
        self.set(tab_name)

        tab_content = self.tab(tab_name)
        tab_content.grid_rowconfigure(0, weight=1)
        tab_content.grid_columnconfigure(0, weight=1)

        reco_frame = RecoFrame(tab_content, tabview=self)
        reco_frame.grid(row=0, column=0, sticky="nsew")

    def close_current_tab(self):
        current_tab = self.get()
        if not current_tab:
            return

        # Prevent closing Step 1
        if current_tab == "Step 1":
            messagebox.showinfo("Protected Tab", "Step 1 cannot be closed.")
            return

        answer = messagebox.askyesno("Confirm Close", f"Are you sure you want to close '{current_tab}'?")
        if answer:
            self.delete(current_tab)
