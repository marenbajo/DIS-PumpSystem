import customtkinter as ctk
from app.config import LABEL_STYLE, TEXT_STYLE
from components.timer_frame import TimerFrame
from components.buttons_frame import ButtonFrame

class StepFrame(ctk.CTkFrame):
    def __init__(self, master, tabview=None, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0, minsize=250)

        self.time_interval = [1,3,5,7,10,15,20,25,30,35,40,50,60]
        fields = ["Time (min)", "Waterlevel (m)", "Meter reading",
                  "calculated Meter reading", "Q(m^3/h)"]

        self.StepTestFrame = ctk.CTkFrame(self)
        self.StepTestFrame.grid(row=0, column=0, rowspan=2, sticky="nsew")

        for i, field in enumerate(fields):
            self.StepTestFrame.grid_columnconfigure(i, weight=1, uniform="col")
            headingLabel = ctk.CTkLabel(
                self.StepTestFrame,
                text=field,
                anchor="center",
                **LABEL_STYLE
            )
            headingLabel.grid(row=0, column=i, sticky="nsew", padx=5, pady=(1,1))

        self.row_frames = {}

        for r, interval in enumerate(self.time_interval, start=1):
            self.StepTestFrame.grid_rowconfigure(r, weight=1)

            row_frame = ctk.CTkFrame(self.StepTestFrame, fg_color="transparent", corner_radius=6)
            row_frame.grid(row=r, column=0, columnspan=len(fields)-1, sticky="nsew", padx=2)

            row_frame.grid_rowconfigure(0, weight=1)  # allow vertical stretch
            for f in range(len(fields)-1):
                row_frame.grid_columnconfigure(f, weight=1, uniform="row")

            timeLabel = ctk.CTkLabel(
                row_frame,
                text=str(interval),
                anchor="center",
                **TEXT_STYLE
            )
            timeLabel.grid(row=0, column=0, sticky="nsew", padx=5, pady=(1,1))

            for f in range(1, len(fields)-1):
                stepInput = ctk.CTkEntry(
                    row_frame,
                    placeholder_text=f"{interval} - {fields[f]}",
                    justify="center",
                    height=30,  # taller entry field
                    **TEXT_STYLE
                )
                stepInput.grid(row=0, column=f, sticky="nsew", padx=5, pady=(1,1))

            self.row_frames[str(interval)] = row_frame

            if r == 1:
                QstepInput = ctk.CTkEntry(
                    self.StepTestFrame,
                    placeholder_text="Q (m^3/h)",
                    justify="center",
                    height=30,
                    **TEXT_STYLE
                )
                QstepInput.grid(row=r, column=len(fields)-1, padx=5, pady=(1,1), sticky="nsew")

        self.timer = TimerFrame(self, time_intervals=self.time_interval, width=230)
        self.timer.grid(row=0, column=1, padx=10, pady=10, sticky="new")
        self.timer.grid_propagate(False)
        self.timer.on_time_change = self.highlight_row

        if tabview is not None:
            self.buttons = ButtonFrame(self, tabview, width=230)
            self.buttons.grid(row=1, column=1, padx=10, pady=10, sticky="sew")
            self.buttons.grid_propagate(False)

    def highlight_row(self, active_time: str):
        for time, frame in self.row_frames.items():
            frame.configure(fg_color="#8080CC" if time == active_time else "transparent")
