import customtkinter as ctk
from components.timer_frame import TimerFrame
from components.buttons_frame import ButtonFrame

class RecoFrame(ctk.CTkFrame):
    def __init__(self, master, tabview=None, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        self.time_interval_l = [1,3,5,7,10,15,20,25,30,35,40]
        self.time_interval_r = [50,60,70,80,90,100,120,250,180, 210,240]
        fields = ["Time (min)", "Waterlevel (m)", "s", "Time (min)", "Waterlevel (m)", "s"]

        # Table
        RecoTestFrame = ctk.CTkFrame(self)
        RecoTestFrame.grid(row=0, column=0, rowspan=2, sticky="nsew")

        for i, field in enumerate(fields):
            RecoTestFrame.grid_columnconfigure(i, weight=1)
            headingLabel = ctk.CTkLabel(RecoTestFrame, text=field)
            headingLabel.grid(row=0, column=i, sticky="nsew")

        # Left side
        for i, interval in enumerate(self.time_interval_l):
            RecoTestFrame.grid_rowconfigure(i+1, weight=1)
            timeLabel_l = ctk.CTkLabel(RecoTestFrame, text=interval)
            timeLabel_l.grid(row=i+1, column=0, sticky="nsew")

            for f in range(1, len(fields)-1):
                stepInput_l = ctk.CTkEntry(
                    RecoTestFrame,
                    placeholder_text=f"{interval} - {fields[f]}"
                )
                stepInput_l.grid(row=i+1, column=f, sticky="nsew", padx=5, pady=5)

        # Right side
        for i, interval in enumerate(self.time_interval_r):
            RecoTestFrame.grid_rowconfigure(i + 1, weight=1)
            timeLabel_r = ctk.CTkLabel(RecoTestFrame, text=interval)
            timeLabel_r.grid(row=i + 1, column=3, sticky="nsew")

            for f in range(4, 6):
                stepInput_r = ctk.CTkEntry(
                    RecoTestFrame,
                    placeholder_text=f"{interval} - {fields[f]}"
                )
                stepInput_r.grid(row=i + 1, column=f, sticky="nsew", padx=5, pady=5)

        # Timer
        self.time_interval = self.time_interval_l + self.time_interval_r
        self.timer = TimerFrame(self, time_intervals=self.time_interval, width=230)
        self.timer.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.timer.grid_propagate(False)

        # Buttons (only if a tabview is provided)
        if tabview is not None:
            self.buttons = ButtonFrame(self, tabview, width=230)
            self.buttons.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
            self.buttons.grid_propagate(False)
