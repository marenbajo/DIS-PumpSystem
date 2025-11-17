import customtkinter as ctk
import random

class TestnumberFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        test_num =  random.randint(1, 100)
        self.test_num = test_num

        self.logo_label = ctk.CTkLabel(
            self,
            text=(f"Test Number: {test_num}"),
            font=("Times New Roman", 20, "bold"),
            text_color="#000099",
        )
        self.logo_label.grid(row=0, column=0, sticky="nsew")