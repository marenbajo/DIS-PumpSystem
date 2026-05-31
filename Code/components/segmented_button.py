import customtkinter as ctk
from config import SEGMENTED_STYLE
from customer_info_frame import InfoFrame
from step_reco_tab import StepRecoTab

class SegmentedButton(ctk.CTkFrame):
    def __init__(self, master, folder_path, test_number, date_value, **kwargs):
        super().__init__(master, **kwargs)

        # Store session info
        self.folder_path = folder_path
        self.test_number = test_number
        self.date_value = date_value

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.active_color = "#C0CBFE"
        self.inactive_color = "#BDC1C5"

        self.client_info_button = ctk.CTkButton(
            self,
            text="Client Information",
            **SEGMENTED_STYLE,
            command=lambda: self.show_frame("Client Information")
        )
        self.client_info_button.grid(row=0, column=0, sticky="ew", padx=2, pady=0)

        self.test_button = ctk.CTkButton(
            self,
            text="Test",
            **SEGMENTED_STYLE,
            command=lambda: self.show_frame("Test")
        )
        self.test_button.grid(row=0, column=1, sticky="ew", padx=2, pady=0)

        # Create both frames WITH SESSION INFO
        self.info_frame = InfoFrame(
            self,
            folder_path=self.folder_path,
            test_number=self.test_number,
            date_value=self.date_value
        )

        self.test_frame = StepRecoTab(
            self,
            self.folder_path,
            self.test_number,
            self.date_value
        )

        self.info_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.test_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.show_frame("Client Information")

    def show_frame(self, value):
        if value == "Client Information":
            self.info_frame.tkraise()
            self.client_info_button.configure(fg_color=self.active_color)
            self.test_button.configure(fg_color=self.inactive_color)
        elif value == "Test":
            self.test_frame.tkraise()
            self.test_button.configure(fg_color=self.active_color)
            self.client_info_button.configure(fg_color=self.inactive_color)
