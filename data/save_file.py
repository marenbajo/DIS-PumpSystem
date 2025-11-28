import csv
import datetime
import os
from components.testnumber_frame import get_test_number

BASE_FOLDER = "data_files"

def start_new_session():
    """Create a folder for this test session."""
    test_number = get_test_number()
    date_value = datetime.date.today().strftime("%Y-%m-%d")
    folder_name = f"Pump_Test_{test_number}_{date_value}"
    folder_path = os.path.join(BASE_FOLDER, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path, test_number, date_value

def save_customer_info(info_data: dict, notes: str, folder_path: str, test_number: int, date_value: str):
    filename = os.path.join(folder_path, f"Customer_Information_{test_number}_{date_value}.csv")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Customer_Information"])
        for key, val in info_data.items():
            writer.writerow([key, val])
        writer.writerow(["Notes", notes])
        writer.writerow(["Timestamp", now])
        writer.writerow(["TestNumber", test_number])
    return filename

def save_steps(step_data: dict, folder_path: str, test_number: int, date_value: str, step_name: str):
    filename = os.path.join(folder_path, f"Steps_{test_number}_{date_value}.csv")
    # Append mode so multiple steps are written below each other
    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([step_name])  # label row
        writer.writerow(["Interval", "Values"])
        for interval, values in step_data.items():
            writer.writerow([interval, " | ".join(values)])
        writer.writerow([])  # blank line between steps
    return filename


def save_recoveries(reco_data: dict, folder_path: str, test_number: int, date_value: str, reco_name: str):
    filename = os.path.join(folder_path, f"Recovery_{test_number}_{date_value}.csv")
    # Append mode so multiple recoveries are written below each other
    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([reco_name])  # label row
        for interval, values in reco_data.items():
            writer.writerow([interval, " | ".join(values)])
        writer.writerow([])  # blank line between recoveries
    return filename

