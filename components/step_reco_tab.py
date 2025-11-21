import customtkinter as ctk
from components.step_frame import StepFrame   # normal import at top

class StepRecoTab(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.step_count = 1
        self.reco_count = 0

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # First tab
        self.add(f"Step {self.step_count}")
        self.set(f"Step {self.step_count}")

        # Create StepFrame inside the first tab
        step_frame = StepFrame(self.tab(f"Step {self.step_count}"), tabview=self)
        step_frame.grid(row=0, column=0, sticky="nsew")

    def add_step_tab(self):
        self.step_count += 1
        tab_name = f"Step {self.step_count}"
        self.add(tab_name)
        self.set(tab_name)

        # Create StepFrame inside the new tab
        step_frame = StepFrame(self.tab(tab_name), tabview=self)
        step_frame.grid(row=0, column=0, sticky="nsew")

    def add_reco_tab(self):
        self.reco_count += 1
        tab_name = f"Recovery {self.reco_count}"
        self.add(tab_name)
        self.set(tab_name)
        # RecoveryFrame will go here later
