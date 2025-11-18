import customtkinter as ctk

class StepFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        time = [1, 3, 5, 7, 10, 15, 20, 25, 30, 35, 40, 50, 60]
        fields = ["Time (min)", "Waterlevel (m)", "Meter reading", "calculated Meter reading", "Q(m^3/h)"]

        StepTestFrame = ctk.CTkFrame(self)
        StepTestFrame.grid(row=0, column=0, rowspan = 3, sticky="nsew")

        for i in range(len(time)):
            StepTestFrame.grid_rowconfigure(i, weight=1)
            timeLabel = ctk.CTkLabel(master=StepTestFrame, text=time[i])
            timeLabel.grid(row=(i + 1), column=0, sticky="nsew")

        for i in range(len(fields)):
            StepTestFrame.grid_columnconfigure(i, weight=1)
            headingLabel = ctk.CTkLabel(master=StepTestFrame, text=fields[(i)])
            headingLabel.grid(row=0, column=i, sticky="nsew")

        for t in range(len(time)):
            for f in range(1, len(fields) - 1):

                stepInput = ctk.CTkEntry(master=StepTestFrame, placeholder_text=(time[t], fields[f]))
                stepInput.grid(row=(t + 1), column=(f), sticky="nsew", padx =5, pady =5)

        QstepInput = ctk.CTkEntry(master=StepTestFrame, placeholder_text="Q (m^3/h)")
        QstepInput.grid(row = 1, column = 4, sticky = "nsew", padx =5, pady =5)