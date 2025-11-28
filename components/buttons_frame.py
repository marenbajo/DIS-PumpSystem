import customtkinter as ctk
from tkinter import messagebox
from app.config import BUTTON_STYLE

class ButtonFrame(ctk.CTkFrame):
    def __init__(self, master, tabview, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.tabview = tabview

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.step_button = ctk.CTkButton(
            self,
            text="Step",
            **BUTTON_STYLE,
            command=self.tabview.add_step_tab
        )
        self.step_button.grid(row=0, column=0, padx=5, pady=5, sticky="sew")

        self.reco_button = ctk.CTkButton(
            self,
            text="Recovery",
            **BUTTON_STYLE,
            command=self.tabview.add_reco_tab
        )
        self.reco_button.grid(row=0, column=1, padx=5, pady=5, sticky="sew")

        self.close_button = ctk.CTkButton(
            self,
            text="Close Tab",
            **BUTTON_STYLE,
            command=self.tabview.close_current_tab
        )
        self.close_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="sew")

        self.save_button = ctk.CTkButton(
            self,
            text="Save",
            **BUTTON_STYLE,
            command=self.tabview.save_current_tab
        )
        self.save_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="sew")

        self.done_button = ctk.CTkButton(
            self,
            text="Done",
            **BUTTON_STYLE,
        )
        self.done_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="sew")
