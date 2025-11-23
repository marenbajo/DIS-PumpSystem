import customtkinter as ctk
from app.config import TEXT_STYLE

class NotesFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.note_label = ctk.CTkLabel(
            self,
            text="Extra Notes: ",
            **TEXT_STYLE,
        )
        self.note_label.grid(row=0, column=0, sticky="w")

        self.notes =ctk.CTkTextbox(self)
        self.notes.grid(row=1, column=0, sticky="nsew")
