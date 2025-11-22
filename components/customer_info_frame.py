import customtkinter as ctk
from components.notes_frame import NotesFrame

class InfoFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.entries = {}

        for r in range(5):
            self.grid_rowconfigure(r, weight=1, uniform="row")
        for c in range(6):
            self.grid_columnconfigure(c, weight=1, uniform="column")

        fields_l = [
            "Client Name: ",
            "Farm Name: ",
            "Borehole depth: ",
            "Latitude (ºS): "
        ]

        fields_c = [
            "Date: ",
            "Borehole Number: ",
            "Borehole size: ",
            "Longitude (ºE): "
        ]

        fields_r = [
            "Time: ",
            "Borehole location/Name: ",
            "Collar height\n(Level before pumping):",
            "Elevation: "
        ]

        for r, field in enumerate(fields_l):
            self.add_field(r, 0, field)

        for r, field in enumerate(fields_c):
            self.add_field(r, 2, field)

        for r, field in enumerate(fields_r):
            self.add_field(r, 4, field)

        self.notes_frame = NotesFrame(self)
        self.notes_frame.grid(row=4, column=0, rowspan=2, columnspan=6, padx=10, pady=(10, 0), sticky="sew")

        self.save_button = ctk.CTkButton(
            self,
            text="Save All",
            font=("Times New Roman", 18)
        )
        self.save_button.grid(row=6, column=0, columnspan=6, pady=(10, 10), padx=10, sticky="e")

    def add_field(self, row, col, text):
        label = ctk.CTkLabel(
            self,
            text=text,
            font=("Times New Roman", 18),
            text_color="black",
            anchor="e"
        )
        label.grid(row=row, column=col, padx=(10, 5), pady=5, sticky="w")

        entry = ctk.CTkEntry(
            self,
            placeholder_text=f"Enter {text.replace(':', '').replace('\n', ' ')}",
            font=("Times New Roman", 18),
            text_color="black",
        )
        entry.grid(row=row, column=col + 1, padx=(5, 10), pady=5, sticky="w")

        self.entries[text.strip()] = entry
