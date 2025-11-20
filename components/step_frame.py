import customtkinter as ctk
from components.timer_frame import TimerFrame

class StepFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        self.time_interval = [1, 3, 5, 7, 10, 15, 20, 25, 30, 35, 40, 50, 60]
        fields = ["Time (min)", "Waterlevel (m)", "Meter reading", "calculated Meter reading", "Q(m^3/h)"]

        StepTestFrame = ctk.CTkFrame(self)
        StepTestFrame.grid(row=0, column=0, sticky="nsew")

        for i in range(len(self.time_interval)):
            StepTestFrame.grid_rowconfigure(i, weight=1)
            timeLabel = ctk.CTkLabel(master=StepTestFrame, text=self.time_interval[i])
            timeLabel.grid(row=(i + 1), column=0, sticky="nsew")

        for i in range(len(fields)):
            StepTestFrame.grid_columnconfigure(i, weight=1)
            headingLabel = ctk.CTkLabel(master=StepTestFrame, text=fields[(i)])
            headingLabel.grid(row=0, column=i, sticky="nsew")

        for t in range(len(self.time_interval)):
            for f in range(1, len(fields) - 1):
                stepInput = ctk.CTkEntry(master=StepTestFrame, placeholder_text=(self.time_interval[t], fields[f]))
                stepInput.grid(row=(t + 1), column=(f), sticky="nsew", padx =5, pady =5)

        QstepInput = ctk.CTkEntry(master=StepTestFrame, placeholder_text="Q (m^3/h)")
        QstepInput.grid(row = 1, column = 4, padx =5, pady =5, sticky = "nsew")

        self.timer = TimerFrame(self, time_intervals=self.time_interval, width=230)
        self.timer.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.timer.grid_propagate(False)

