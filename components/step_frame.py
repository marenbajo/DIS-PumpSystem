import customtkinter as ctk
import datetime
from app.config import LABEL_STYLE, TEXT_STYLE, HIGHLIGHT_STYLE
from components.timer_frame import TimerFrame
from components.buttons_frame import ButtonFrame
from data.save_file import save_steps, start_new_session

class StepFrame(ctk.CTkFrame):
    def __init__(self, master, tabview=None, step_name="Step 1", status_label=None, autosave_interval=60000, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.step_name = step_name
        self.folder_path, self.test_number, self.date_value = start_new_session()

        # Shared status label
        self.status_label = status_label
        self.autosave_interval = autosave_interval
        if not self.status_label:
            self.status_label = ctk.CTkLabel(self, text="", font=("Times New Roman", 12))
            self.status_label.grid(row=99, column=0, columnspan=6, pady=(5, 5), sticky="w")

        # Layout
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0, minsize=250)

        self.time_interval = [1,3,5,7,10,15,20,25,30,35,40,50,60]
        fields = ["Time (min)", "Waterlevel (m)", "Meter reading",
                  "Calculated Meter reading", "Q(m^3/h)"]

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

        # Store row references
        self.row_frames = {}

        for r, interval in enumerate(self.time_interval, start=1):
            self.StepTestFrame.grid_rowconfigure(r, weight=1)

            row_frame = ctk.CTkFrame(self.StepTestFrame, fg_color="transparent", corner_radius=6)
            row_frame.grid(row=r, column=0, columnspan=len(fields)-1, sticky="nsew", padx=2)

            row_frame.grid_rowconfigure(0, weight=1)
            for f in range(len(fields)-1):
                row_frame.grid_columnconfigure(f, weight=1, uniform="row")

            # Time label
            timeLabel = ctk.CTkLabel(
                row_frame,
                text=str(interval),
                anchor="center",
                **TEXT_STYLE
            )
            timeLabel.grid(row=0, column=0, sticky="nsew", padx=5, pady=(1,1))

            # Waterlevel entry
            water_entry = ctk.CTkEntry(
                row_frame,
                placeholder_text=f"{interval} - Waterlevel",
                justify="center",
                height=28,
                **TEXT_STYLE
            )
            water_entry.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

            # Meter reading entry
            meter_entry = ctk.CTkEntry(
                row_frame,
                placeholder_text=f"{interval} - Meter reading",
                justify="center",
                height=28,
                **TEXT_STYLE
            )
            meter_entry.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

            # Calculated meter reading (disabled entry so it looks the same)
            calc_entry = ctk.CTkEntry(
                row_frame,
                justify="center",
                height=28,
                **TEXT_STYLE
            )
            calc_entry.insert(0, "")
            calc_entry.configure(state="disabled")
            calc_entry.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)

            # Store references
            self.row_frames[str(interval)] = {
                "frame": row_frame,
                "water_entry": water_entry,
                "meter_entry": meter_entry,
                "calc_entry": calc_entry
            }

            # Q entry only once, in first row
            if r == 1:
                self.q_entry = ctk.CTkEntry(
                    self.StepTestFrame,
                    placeholder_text="Q (m^3/h)",
                    justify="center",
                    height=30,
                    **TEXT_STYLE
                )
                self.q_entry.grid(row=r, column=len(fields)-1, padx=5, pady=5, sticky="nsew")
                self.q_entry.bind("<KeyRelease>", lambda e: self.update_calculated())

        # Timer
        self.timer = TimerFrame(self, time_intervals=self.time_interval, width=200)
        self.timer.grid(row=0, column=1, padx=10, pady=10, sticky="new")
        self.timer.grid_propagate(False)
        self.timer.on_time_change = self.highlight_row

        # Buttons
        if tabview is not None:
            self.buttons = ButtonFrame(self, tabview, width=200)
            self.buttons.grid(row=1, column=1, padx=10, pady=10, sticky="sew")

        # Autosave
        self.schedule_autosave()

    # ----- Highlight -----
    def highlight_row(self, active_time: str):
        for time, row in self.row_frames.items():
            if time == active_time:
                row["frame"].configure(**HIGHLIGHT_STYLE)
            else:
                row["frame"].configure(fg_color="transparent")

    # ----- Calculated Meter Reading -----
    def update_calculated(self):
        q_val = self.q_entry.get().strip()
        if not q_val:
            for row in self.row_frames.values():
                row["calc_entry"].configure(state="normal")
                row["calc_entry"].delete(0, "end")
                row["calc_entry"].configure(state="disabled")
            return

        try:
            q = float(q_val)
        except ValueError:
            for row in self.row_frames.values():
                row["calc_entry"].configure(state="normal")
                row["calc_entry"].delete(0, "end")
                row["calc_entry"].configure(state="disabled")
            return

        for interval, row in self.row_frames.items():
            minutes = int(interval)
            result = minutes / q
            row["calc_entry"].configure(state="normal")
            row["calc_entry"].delete(0, "end")
            row["calc_entry"].insert(0, f"{result:.2f}")
            row["calc_entry"].configure(state="disabled")

    # ----- Data Collection -----
    def collect_data(self):
        step_data = {}
        for interval, row in self.row_frames.items():
            values = [
                row["water_entry"].get(),
                row["meter_entry"].get(),
                row["calc_entry"].get()
            ]
            step_data[interval] = values
        return step_data

    def save_data(self):
        step_data = self.collect_data()
        q_value = self.q_entry.get()
        filename = save_steps(step_data, q_value, self.folder_path, self.test_number, self.date_value, self.step_name)
        now = datetime.datetime.now()
        if self.status_label:
            self.status_label.configure(
                text=f"Saved {self.step_name} for Test {self.test_number} at {now.strftime('%Y-%m-%d %H:%M')}"
            )
        print(f"[Manual/Auto Save] {self.step_name} updated in {filename}")

    def schedule_autosave(self):
        self.save_data()
        self.after(self.autosave_interval, self.schedule_autosave)
