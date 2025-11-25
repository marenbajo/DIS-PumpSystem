import customtkinter as ctk
from app.config import TEXT_STYLE, SEGMENTED_STYLE
from components.customer_info_frame import InfoFrame
from components.step_reco_tab import StepRecoTab

class SegmentedButton(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=0)   # segmented button row
        self.grid_rowconfigure(1, weight=1)   # frame row expands
        self.grid_columnconfigure(0, weight=1)

        self.segmented_button = ctk.CTkSegmentedButton(
            self,
            values=["Client Information", "Test"],
            **SEGMENTED_STYLE,
            **TEXT_STYLE,
            command=self.show_frame
        )
        self.segmented_button.set("Client Information")
        self.segmented_button.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.segmented_button.grid_columnconfigure(0, weight=1)

        self.info_frame = InfoFrame(self)
        self.test_frame = StepRecoTab(self)
        self.show_frame("Client Information")

    def show_frame(self, value):
        self.test_frame.grid_forget()
        if value == "Client Information":
            self.info_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        elif value == "Test":
            self.test_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
