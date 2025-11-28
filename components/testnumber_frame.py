import customtkinter as ctk
from app.config import TEST_NUM_STYLE
import os

_current_test_number = 0

def next_test_number():
    global _current_test_number
    _current_test_number += 1
    return _current_test_number

def get_test_number():
    global _current_test_number
    return _current_test_number

class TestnumberFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.test_num = next_test_number()

        self.logo_label = ctk.CTkLabel(
            self,
            text=f"Test Number: {self.test_num}",
            **TEST_NUM_STYLE
        )
        self.logo_label.grid(row=0, column=0, sticky="nsew")
