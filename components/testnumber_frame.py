import customtkinter as ctk
from app.config import TEST_NUM_STYLE
import os

BASE_FOLDER = "data_files"
_current_test_number = 0


def _scan_existing_tests():
    """Return the highest test number found in BASE_FOLDER."""
    if not os.path.exists(BASE_FOLDER):
        os.makedirs(BASE_FOLDER, exist_ok=True)
        return 0

    numbers = []
    for name in os.listdir(BASE_FOLDER):
        if name.startswith("Pump_Test_"):
            parts = name.split("_")
            # Folder format: Pump_Test_<num>_<date>
            if len(parts) >= 3 and parts[2].isdigit():
                numbers.append(int(parts[2]))
    return max(numbers, default=0)


def next_test_number():
    """Increment based on existing folders, not just a global counter."""
    global _current_test_number
    if _current_test_number == 0:
        # initialize from existing folders
        _current_test_number = _scan_existing_tests()
    _current_test_number += 1
    return _current_test_number


def get_test_number():
    """Return the current test number (after next_test_number has been called)."""
    global _current_test_number
    return _current_test_number


class TestnumberFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Generate a new test number for this session
        self.test_num = next_test_number()

        # Display the test number
        self.logo_label = ctk.CTkLabel(
            self,
            text=f"Test Number: {self.test_num}",
            **TEST_NUM_STYLE
        )
        self.logo_label.grid(row=0, column=0, sticky="nsew")
