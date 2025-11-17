import customtkinter as ctk

class SegmentedButton(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.segmented_button = ctk.CTkSegmentedButton(
            self,
            values=["Client Information", "Test"],
            selected_color = "#bababa",
            unselected_color = "#e2e2e2",
            selected_hover_color = "#808080",
            font = ("Times New Roman", 14),
            text_color =("#000000")
            # command=segmented_button_callback
        )
        self.segmented_button.set("Client Information")
        self.segmented_button.grid(row=0, column=0, sticky="nsew")