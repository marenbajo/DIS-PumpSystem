import customtkinter as ctk
from components.timer_frame import TimerFrame
from components.buttons_frame import ButtonFrame

class StepFrame(ctk.CTkFrame):
    def __init__(self, master, tabview=None, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        # Grid setup
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0, minsize=250)

        self.time_interval = [1,3,5,7,10,15,20,25,30,35,40,50,60]
        fields = ["Time (min)", "Waterlevel (m)", "Meter reading",
                  "calculated Meter reading", "Q(m^3/h)"]

        # Table
        StepTestFrame = ctk.CTkFrame(self)
        StepTestFrame.grid(row=0, column=0, rowspan=2, sticky="nsew")

        for i, field in enumerate(fields):
            StepTestFrame.grid_columnconfigure(i, weight=1)
            headingLabel = ctk.CTkLabel(StepTestFrame, text=field)
            headingLabel.grid(row=0, column=i, sticky="nsew")

        for i, interval in enumerate(self.time_interval):
            StepTestFrame.grid_rowconfigure(i+1, weight=1)
            timeLabel = ctk.CTkLabel(StepTestFrame, text=interval)
            timeLabel.grid(row=i+1, column=0, sticky="nsew")

            for f in range(1, len(fields)-1):
                stepInput = ctk.CTkEntry(
                    StepTestFrame,
                    placeholder_text=f"{interval} - {fields[f]}"
                )
                stepInput.grid(row=i+1, column=f, sticky="nsew", padx=5, pady=5)

        QstepInput = ctk.CTkEntry(StepTestFrame, placeholder_text="Q (m^3/h)")
        QstepInput.grid(row=1, column=4, padx=5, pady=5, sticky="nsew")

        # Timer
        self.timer = TimerFrame(self, time_intervals=self.time_interval, width=230)
        self.timer.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.timer.grid_propagate(False)

        # Buttons (only if a tabview is provided)
        if tabview is not None:
            self.buttons = ButtonFrame(self, tabview, width=230)
            self.buttons.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
            self.buttons.grid_propagate(False)
