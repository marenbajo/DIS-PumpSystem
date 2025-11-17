import customtkinter as ctk
from app.config import configure_theme
from app.layout import layout_config
from icon_choice import set_app_icon
from components.logo_frame import LogoFrame
from components.testnumber_frame import TestnumberFrame
from components.segmented_button import SegmentedButton


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pump System")
        set_app_icon(self)

        configure_theme()
        layout_config(self)

        self.logo_frame = LogoFrame(self, height=100)
        self.logo_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.testnumber_frame = TestnumberFrame(self, height=100)
        self.testnumber_frame.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsew")

        self.segmented_button = SegmentedButton(self)
        self.segmented_button.grid(row=1, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()

