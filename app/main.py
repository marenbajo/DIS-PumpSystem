import customtkinter as ctk
from app.config import configure_theme
from app.layout import layout_config
from icon_choice import set_app_icon


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pump System")
        set_app_icon(self)

        configure_theme()
        layout_config(self)



if __name__ == "__main__":
    app = App()
    app.mainloop()

