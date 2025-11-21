import customtkinter as ctk
import threading
import time

class TimerFrame(ctk.CTkFrame):
    def __init__(self, master, time_intervals=None, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        # Use provided intervals or default
        self.time_intervals = time_intervals
        self.current_index = 0
        self.remaining_minutes = self.time_intervals[self.current_index]
        self.running = False
        self.thread = None

        # Outer frame with fixed size
        self.timer_frame = ctk.CTkFrame(self, width=200, height=120)
        self.timer_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.timer_frame.grid_propagate(False)   # keep fixed size

        # Label at top
        self.label = ctk.CTkLabel(self.timer_frame, text=f"{self.remaining_minutes} min",
                                  font=("Times New Roman", 24))
        self.label.grid(row=0, column=0, columnspan=2, pady=(10, 5), sticky="ew")

        # Buttons row (Start + Pause side by side)
        self.start_button = ctk.CTkButton(self.timer_frame, text="Start", command=self.start_timer)
        self.start_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.pause_button = ctk.CTkButton(self.timer_frame, text="Pause", command=self.pause_timer)
        self.pause_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Restart button below
        self.restart_button = ctk.CTkButton(self.timer_frame, text="Restart", command=self.restart_timer)
        self.restart_button.grid(row=2, column=0, columnspan=2, padx=5, pady=(5,10), sticky="ew")

        # Configure grid inside timer_frame
        self.timer_frame.grid_rowconfigure(0, weight=0)
        self.timer_frame.grid_rowconfigure(1, weight=0)
        self.timer_frame.grid_rowconfigure(2, weight=0)
        self.timer_frame.grid_columnconfigure(0, weight=1)
        self.timer_frame.grid_columnconfigure(1, weight=1)

    def update_label(self):
        self.label.configure(text=f"{self.remaining_minutes} min (Step {self.current_index+1}/{len(self.time_intervals)})")

    def countdown(self):
        while self.running and self.current_index < len(self.time_intervals):
            while self.running and self.remaining_minutes > 0:
                time.sleep(60)  # wait 1 minute
                if self.running:
                    self.remaining_minutes -= 1
                    self.update_label()

            # Move to next interval
            if self.running:
                self.current_index += 1
                if self.current_index < len(self.time_intervals):
                    self.remaining_minutes = self.time_intervals[self.current_index]
                    self.update_label()
                else:
                    self.running = False  # finished all intervals

    def start_timer(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.countdown, daemon=True)
            self.thread.start()

    def pause_timer(self):
        self.running = False

    def restart_timer(self):
        self.running = False
        self.current_index = 0
        self.remaining_minutes = self.time_intervals[self.current_index]
        self.update_label()
