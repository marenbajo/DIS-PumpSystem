import customtkinter as ctk
from app.config import configure_theme
from app.layout import layout_config
from data.save_file import start_new_session
from app.icon_choice import set_app_icon
from components.logo_frame import LogoFrame
from components.segmented_button import SegmentedButton

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pump System")
        set_app_icon(self)

        configure_theme()
        layout_config(self)

        # Start a new test session
        folder_path, test_number, date_value = start_new_session()

        # Store them on the App instance (optional but useful)
        self.folder_path = folder_path
        self.test_number = test_number
        self.date_value = date_value

        self.logo_frame = LogoFrame(self, height=100)
        self.logo_frame.grid(row=0, column=0, padx=10, pady=(20,20), sticky="nsew")

        # Pass session info into SegmentedButton
        self.segmented_button = SegmentedButton(
            self,
            folder_path,
            test_number,
            date_value
        )
        self.segmented_button.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()