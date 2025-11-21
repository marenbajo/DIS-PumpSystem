import customtkinter as ctk

class ButtonFrame(ctk.CTkFrame):
    def __init__(self, master, tabview, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.tabview = tabview

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.step_button = ctk.CTkButton(
            self, text="Step", height=120,
            command=self.tabview.add_step_tab
        )
        self.step_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.reco_button = ctk.CTkButton(
            self, text="Recovery", height=120,
            command=self.tabview.add_reco_tab
        )
        self.reco_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.done_button = ctk.CTkButton(
            self, text="Done", height=120, width=200
        )
        self.done_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
