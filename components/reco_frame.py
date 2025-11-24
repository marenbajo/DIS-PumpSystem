import customtkinter as ctk
from app.config import LABEL_STYLE, TEXT_STYLE
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
        self.time_interval_r = [50,60,70,80,90,100,120,250,180,210,240]
        fields = ["Time (min)", "Waterlevel (m)", "s", "Time (min)", "Waterlevel (m)", "s"]

        # Table
        self.RecoTestFrame = ctk.CTkFrame(self)
        self.RecoTestFrame.grid(row=0, column=0, rowspan=2, sticky="nsew")

        for i, field in enumerate(fields):
            self.RecoTestFrame.grid_columnconfigure(i, weight=1, uniform="col")
            headingLabel = ctk.CTkLabel(self.RecoTestFrame, text=field, anchor="center", **LABEL_STYLE)
            headingLabel.grid(row=0, column=i, sticky="nsew", padx=5, pady=1)

        # Store row frames for highlighting
        self.row_frames = {}

        # Left side rows
        for r, interval in enumerate(self.time_interval_l, start=1):
            self.RecoTestFrame.grid_rowconfigure(r, weight=1)

            row_frame = ctk.CTkFrame(self.RecoTestFrame, fg_color="transparent", corner_radius=6)
            row_frame.grid(row=r, column=0, columnspan=3, sticky="nsew", padx=2)

            row_frame.grid_rowconfigure(0, weight=1)
            for c in range(3):
                row_frame.grid_columnconfigure(c, weight=1, uniform="row")

            timeLabel = ctk.CTkLabel(row_frame, text=str(interval), anchor="center", **TEXT_STYLE)
            timeLabel.grid(row=0, column=0, sticky="nsew", padx=5, pady=1)

            for f in range(1, 3):
                entry = ctk.CTkEntry(
                    row_frame,
                    placeholder_text=f"{interval} - {fields[f]}",
                    justify="center",
                    height=30,
                    **TEXT_STYLE
                )
                entry.grid(row=0, column=f, sticky="nsew", padx=5, pady=1)

            self.row_frames[str(interval)] = row_frame

        # Right side rows
        for r, interval in enumerate(self.time_interval_r, start=1):
            row_index = r  # reuse same row index range
            self.RecoTestFrame.grid_rowconfigure(row_index, weight=1)

            row_frame = ctk.CTkFrame(self.RecoTestFrame, fg_color="transparent", corner_radius=6)
            row_frame.grid(row=row_index, column=3, columnspan=3, sticky="nsew", padx=2)

            row_frame.grid_rowconfigure(0, weight=1)
            for c in range(3):
                row_frame.grid_columnconfigure(c, weight=1, uniform="row")

            timeLabel = ctk.CTkLabel(row_frame, text=str(interval), anchor="center", **TEXT_STYLE)
            timeLabel.grid(row=0, column=0, sticky="nsew", padx=5, pady=1)

            for f in range(4, 6):
                entry = ctk.CTkEntry(
                    row_frame,
                    placeholder_text=f"{interval} - {fields[f]}",
                    justify="center",
                    height=30,
                    **TEXT_STYLE
                )
                entry.grid(row=0, column=f-3, sticky="nsew", padx=5, pady=1)

            self.row_frames[str(interval)] = row_frame

        # Timer
        self.time_interval = self.time_interval_l + self.time_interval_r
        self.timer = TimerFrame(self, time_intervals=self.time_interval, width=230)
        self.timer.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.timer.grid_propagate(False)
        self.timer.on_time_change = self.highlight_row

        # Buttons
        if tabview is not None:
            self.buttons = ButtonFrame(self, tabview, width=230)
            self.buttons.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
            self.buttons.grid_propagate(False)

    def highlight_row(self, active_time: str):
        for time, frame in self.row_frames.items():
            frame.configure(fg_color="#8080CC" if time == active_time else "transparent")
