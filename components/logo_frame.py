import customtkinter as ctk
from app.config import LOGO_STYLE
from components.testnumber_frame import TestnumberFrame

class LogoFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.logo_label = ctk.CTkLabel(
            self,
            text="DIS Pump Test",
            **LOGO_STYLE
        )
        self.logo_label.grid(row=0, column=0, sticky="nsew")

        test_frame = TestnumberFrame(self)
        test_frame.grid(row=0, column=1, sticky="nsew")
