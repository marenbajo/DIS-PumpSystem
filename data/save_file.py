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

def save_steps(step_data, folder_path, test_number, date_value, step_name):
    filename = os.path.join(folder_path, f"Steps_{test_number}_{date_value}.csv")

    # Load existing rows
    rows = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            rows = list(csv.reader(f))

    # Always ensure header
    header = ["Step", "Time", "Meter reading", "Calculated meter reading", "Q (m³/h)"]
    if not rows or rows[0] != header:
        rows = [header]

    # Remove old block for this step
    filtered = []
    skip_block = False
    for row in rows:
        if row and row[0] == step_name:  # start of block
            skip_block = True
            continue
        if skip_block:
            if row and row[0] != "":  # next step starts
                skip_block = False
                filtered.append(row)
            # else: skip blank rows belonging to this step
        else:
            filtered.append(row)

    # Build new block
    new_rows = []
    first = True
    for interval, values in step_data.items():
        while len(values) < 3:
            values.append("")
        label = step_name if first else ""
        new_rows.append([label, interval] + values)
        first = False

    # Write updated CSV
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(filtered + new_rows)

    return filename

def save_recoveries(reco_data, folder_path, test_number, date_value, reco_name):
    filename = os.path.join(folder_path, f"Recovery_{test_number}_{date_value}.csv")

    # Load existing rows
    rows = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            rows = list(csv.reader(f))

    # Always ensure header
    header = ["Recovery", "Time", "Waterlevel (m)", "s"]
    if not rows or rows[0] != header:
        rows = [header]

    # Remove old block for this recovery
    filtered = []
    skip_block = False
    for row in rows:
        if row and row[0] == reco_name:  # start of block
            skip_block = True
            continue
        if skip_block:
            if row and row[0] != "":  # next recovery starts
                skip_block = False
                filtered.append(row)
            # else: skip blank rows belonging to this recovery
        else:
            filtered.append(row)

    # Build new block
    new_rows = []
    first = True
    for interval, values in reco_data.items():
        clean_interval = "".join([ch for ch in interval if ch.isdigit()])
        while len(values) < 2:
            values.append("")
        label = reco_name if first else ""
        new_rows.append([label, clean_interval] + values)
        first = False

    # Write updated CSV
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(filtered + new_rows)

    return filename
