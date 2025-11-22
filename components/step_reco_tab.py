import customtkinter as ctk
from components.step_frame import StepFrame
from components.reco_frame import RecoFrame

class StepRecoTab(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.step_count = 1
        self.reco_count = 0

        # Make the tabview itself expand
        self.rowconfigure(0, weight=0)
        self.columnconfigure(0, weight=1)

        # First tab
        self.add(f"Step {self.step_count}")
        self.set(f"Step {self.step_count}")

        # Configure the tab content frame to expand
        tab_content = self.tab(f"Step {self.step_count}")
        tab_content.grid_rowconfigure(0, weight=1)
        tab_content.grid_columnconfigure(0, weight=1)

        # Create StepFrame inside the first tab
        step_frame = StepFrame(tab_content, tabview=self)
        step_frame.grid(row=0, column=0, sticky="nsew")

    def add_step_tab(self):
        self.step_count += 1
        tab_name = f"Step {self.step_count}"
        self.add(tab_name)
        self.set(tab_name)

        # Configure the tab content frame to expand
        tab_content = self.tab(tab_name)
        tab_content.grid_rowconfigure(0, weight=1)
        tab_content.grid_columnconfigure(0, weight=1)

        # Create StepFrame inside the new tab
        step_frame = StepFrame(tab_content, tabview=self)
        step_frame.grid(row=0, column=0, sticky="nsew")

    def add_reco_tab(self):
        self.reco_count += 1
        tab_name = f"Recovery {self.reco_count}"
        self.add(tab_name)
        self.set(tab_name)

        # Configure the tab content frame to expand
        tab_content = self.tab(tab_name)
        tab_content.grid_rowconfigure(0, weight=1)
        tab_content.grid_columnconfigure(0, weight=1)

        # Create RecoFrame inside the new tab
        reco_frame = RecoFrame(tab_content, tabview=self)
        reco_frame.grid(row=0, column=0, sticky="nsew")
