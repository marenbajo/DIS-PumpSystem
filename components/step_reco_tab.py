import customtkinter as ctk
from tkinter import messagebox
import os
import csv
from app.config import TEXT_STYLE, SEGMENTED_STYLE
from components.step_frame import StepFrame
from components.reco_frame import RecoFrame

class StepRecoTab(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        # Style segmented button
        self._segmented_button.configure(**TEXT_STYLE, **SEGMENTED_STYLE)

        # Counters
        self.step_count = 1
        self.reco_count = 0

        # Expand tabview
        self.rowconfigure(0, weight=0)
        self.columnconfigure(0, weight=1)

        # First tab (Step 1)
        self.add("Step 1")
        self.set("Step 1")

        tab_content = self.tab("Step 1")
        tab_content.grid_rowconfigure(0, weight=1)
        tab_content.grid_columnconfigure(0, weight=1)

        step_frame = StepFrame(tab_content, tabview=self, step_name="Step 1")
        step_frame.grid(row=0, column=0, sticky="nsew")

        # Keep a reference to frames by tab name
        self.frames = {"Step 1": step_frame}

    def _next_step_number(self):
        existing_steps = [
            int(name.split()[1])
            for name in self._name_list
            if name.startswith("Step")
        ]
        n = 2
        while n in existing_steps:
            n += 1
        return n

    def add_step_tab(self):
        self.step_count = self._next_step_number()
        tab_name = f"Step {self.step_count}"
        self.add(tab_name)
        self.set(tab_name)

        tab_content = self.tab(tab_name)
        tab_content.grid_rowconfigure(0, weight=1)
        tab_content.grid_columnconfigure(0, weight=1)

        step_frame = StepFrame(tab_content, tabview=self, step_name=tab_name)
        step_frame.grid(row=0, column=0, sticky="nsew")

        self.frames[tab_name] = step_frame

    def add_reco_tab(self):
        self.reco_count += 1
        tab_name = f"Recovery {self.reco_count}"
        self.add(tab_name)
        self.set(tab_name)

        tab_content = self.tab(tab_name)
        tab_content.grid_rowconfigure(0, weight=1)
        tab_content.grid_columnconfigure(0, weight=1)

        reco_frame = RecoFrame(tab_content, tabview=self, reco_name=tab_name)
        reco_frame.grid(row=0, column=0, sticky="nsew")

        self.frames[tab_name] = reco_frame

    def close_current_tab(self):
        current_tab = self.get()
        if not current_tab:
            return

        # Prevent closing Step 1
        if current_tab == "Step 1":
            messagebox.showinfo("Protected Tab", "Step 1 cannot be closed.")
            return

        answer = messagebox.askyesno("Confirm Close", f"Are you sure you want to close '{current_tab}'?")
        if not answer:
            return

        frame = self.frames.get(current_tab)
        if frame:
            if current_tab.startswith("Step"):
                self._delete_block_from_csv(
                    os.path.join(frame.folder_path, f"Steps_{frame.test_number}_{frame.date_value}.csv"),
                    current_tab
                )
            elif current_tab.startswith("Recovery"):
                self._delete_block_from_csv(
                    os.path.join(frame.folder_path, f"Recovery_{frame.test_number}_{frame.date_value}.csv"),
                    current_tab
                )

        # Delete tab and frame reference
        self.delete(current_tab)
        if current_tab in self.frames:
            del self.frames[current_tab]

    def _delete_block_from_csv(self, filename, section_name):
        if not os.path.exists(filename):
            return

        with open(filename, "r", encoding="utf-8") as f:
            rows = list(csv.reader(f))

        header = rows[0] if rows else []
        filtered = [header]
        skip_block = False
        for row in rows[1:]:
            if row and row[0] == section_name:  # start of block
                skip_block = True
                continue
            if skip_block:
                if row and row[0] != "":  # next block starts
                    skip_block = False
                    filtered.append(row)
                # else: skip blank rows belonging to this block
            else:
                filtered.append(row)

        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(filtered)

    def save_current_tab(self):
        current_tab = self.get()
        if not current_tab:
            return

        frame = self.frames.get(current_tab)
        if frame and hasattr(frame, "save_data"):
            frame.save_data()
        else:
            messagebox.showinfo("Save", f"No saveable frame found in '{current_tab}'")
