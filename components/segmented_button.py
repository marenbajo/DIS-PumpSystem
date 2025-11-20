import customtkinter as ctk
from components.customer_info_frame import InfoFrame
from components.step_frame import StepFrame

class SegmentedButton(ctk.CTkFrame):
    def __init__(self, master, test_number=1, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.grid_rowconfigure(0, weight=1)   # segmented button row
        self.grid_rowconfigure(1, weight=1)   # frame row expands
        self.grid_columnconfigure(0, weight=1)

        self.segmented_button = ctk.CTkSegmentedButton(
            self,
            values=["Client Information", "Test"],
            selected_color="#bababa",
            unselected_color="#e2e2e2",
            selected_hover_color="#808080",
            font=("Times New Roman", 14),
            text_color="#000000",
            command=self.show_frame
        )
        self.segmented_button.set("Client Information")
        self.segmented_button.grid(row=0, column=0, sticky="ew", pady=10)

        self.info_frame = InfoFrame(self, test_number)
        self.test_frame = StepFrame(self)
        self.show_frame("Client Information")

    def show_frame(self, value):
        if value == "Client Information":
            self.info_frame.grid(row=1, column=0, sticky="nsew")
        elif value == "Test":
            self.test_frame.grid(row=1, column=0, sticky="nsew")
