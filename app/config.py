import customtkinter as ctk

def configure_theme():
    ctk.set_appearance_mode("Light")
    ctk.set_default_color_theme("dark-blue")

LOGO_STYLE = {
    "font": ("Times New Roman", 30, "bold"),
    "text_color": "#1649C4",
}

TEST_NUM_STYLE = {
    "font": ("Times New Roman", 20, "bold"),
    "text_color": "#1649C4",
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
    "fg_color": "#C0CBFE",
    "hover_color": "#6964F3",
    "border_color": "#6964F3",
    "border_width": 2,
    "height": 60,
    "width": 100
}

TIMER_BUTTON_STYLE = {
    "font": ("Times New Roman", 16, "bold"),
    "text_color": "black",
    "fg_color": "#C0CBFE",
    "border_color": "#6964F3",
    "hover_color": "#6964F3",
    "border_width": 2,
    "height": 40,
    "width": 100
}

TIMER_STYLE = {
    "fg_color": "white",
    "border_color": "#6964F3",
    "border_width": 2,
}

HIGHLIGHT_STYLE = {
    "fg_color": "#C0CBFE",
}

SEGMENTED_STYLE = {
    "selected_color" : "#C0CBFE",
    "selected_hover_color" : "#6964F3",
    "unselected_color" : "#BDC1C5",
    "unselected_hover_color" : "#6964F3"
}
