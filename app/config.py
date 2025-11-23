import customtkinter as ctk

def configure_theme():
    ctk.set_appearance_mode("Light")
    ctk.set_default_color_theme("dark-blue")
LOGO_STYLE = {
    "font": ("Times New Roman", 30, "bold"),
    "text_color": "#3434ef",
}

TEST_NUM_STYLE = {
    "font": ("Times New Roman", 20, "bold"),
    "text_color": "#3434ef",
}

LABEL_STYLE = {
    "font": ("Times New Roman", 18, "bold"),
    "text_color": "black",
}

TEXT_STYLE = {
    "font": ("Times New Roman", 16,),
    "text_color": "black",
}

BUTTON_STYLE = {
    "font": ("Times New Roman", 16, "bold"),
    "text_color": "black",
    "fg_color": "#b9b9b9",
    "border_width": 2,
    "border_color": "#3434ef",
    "height": 60,
    "width": 100
}

TIMER_BUTTON_STYLE = {
    "font": ("Times New Roman", 16, "bold"),
    "text_color": "black",
    "fg_color": "#b9b9b9",
    "border_width": 2,
    "border_color": "#3434ef",
    "height": 40,
    "width": 100
}
