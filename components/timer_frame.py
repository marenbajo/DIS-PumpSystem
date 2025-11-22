import customtkinter as ctk

class TimerFrame(ctk.CTkFrame):
    def __init__(self, master, time_intervals, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        # Convert intervals (minutes) to integers
        self.time_intervals = [int(t) for t in time_intervals]
        self.total_steps = len(self.time_intervals)

        # State
        self.current_index = 0
        self.remaining_seconds = self.time_intervals[self.current_index] * 60
        self.running = False
        self.after_id = None

        # Outer frame with fixed size
        self.timer_frame = ctk.CTkFrame(self, width=200, height=120)
        self.timer_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.timer_frame.grid_propagate(False)   # keep fixed size

        # Label at top
        self.label = ctk.CTkLabel(
            self.timer_frame,
            text=self._format_time(),
            font=("Times New Roman", 24)
        )
        self.label.grid(row=0, column=0, columnspan=2, pady=(10, 5), sticky="ew")

        # Buttons row (Start + Pause side by side)
        self.play_button = ctk.CTkButton(self.timer_frame, text="Start", command=self.start_countdown)
        self.play_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.pause_button = ctk.CTkButton(self.timer_frame, text="Pause", command=self.pause_countdown)
        self.pause_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Restart button below
        self.reset_button = ctk.CTkButton(self.timer_frame, text="Restart", command=self.reset_countdown)
        self.reset_button.grid(row=2, column=0, columnspan=2, padx=5, pady=(5,10), sticky="ew")

        # Configure grid inside timer_frame
        self.timer_frame.grid_rowconfigure(0, weight=0)
        self.timer_frame.grid_rowconfigure(1, weight=0)
        self.timer_frame.grid_rowconfigure(2, weight=0)
        self.timer_frame.grid_columnconfigure(0, weight=1)
        self.timer_frame.grid_columnconfigure(1, weight=1)

        # Optional callback for external highlight
        self.on_time_change = None

    # ----- Helpers -----
    def _format_time(self):
        mins = self.remaining_seconds // 60
        secs = self.remaining_seconds % 60
        return f"{mins}:{secs:02d}"

    def _update_label(self):
        self.label.configure(text=self._format_time())

    # ----- Countdown logic -----
    def _tick(self):
        if not self.running:
            return

        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1
            self._update_label()

            # Fire callback when a full minute boundary is hit
            if self.remaining_seconds % 60 == 0 and self.on_time_change:
                minutes = self.remaining_seconds // 60
                if minutes in self.time_intervals:
                    self.on_time_change(str(minutes))

            self.after_id = self.after(1000, self._tick)
        else:
            # Move to next interval
            self.current_index += 1
            if self.current_index < self.total_steps:
                self.remaining_seconds = self.time_intervals[self.current_index] * 60
                self._update_label()
                self.after_id = self.after(1000, self._tick)
            else:
                # Finished all intervals
                self.running = False
                self.after_id = None

    # ----- Controls -----
    def start_countdown(self):
        if not self.running:
            self.running = True
            self._tick()

    def pause_countdown(self):
        self.running = False
        if self.after_id:
            self.after_cancel(self.after_id)
            self.after_id = None

    def reset_countdown(self):
        self.pause_countdown()
        self.remaining_seconds = self.time_intervals[self.current_index] * 60
        self._update_label()

    def set_time_index(self, index):
        """Switch to a different interval in the sequence."""
        if 0 <= index < len(self.time_intervals):
            self.current_index = index
            self.remaining_seconds = self.time_intervals[index] * 60
            self._update_label()
            if self.on_time_change:
                self.on_time_change(str(self.time_intervals[index]))
