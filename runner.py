import papermill as pm
from datetime import datetime, timedelta
import os

expiry_date_str="2025-06-26"
expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d")
def get_start_day():
    # Go back 15 weekdays
    d = expiry_date
    count = 0
    while count < 15:
        d -= timedelta(days=1)
        if d.weekday() < 5:
            count += 1
    return d

def get_next_day(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    dt += timedelta(days=1)
    while dt.weekday() >= 5:  # Skip weekends
        dt += timedelta(days=1)
    return dt

def run_until_expiry():
    # === Check or create day_info.txt ===
    if not os.path.exists("day_info.txt"):
        start_day = get_start_day()
        with open("day_info.txt", "w") as f:
            f.write(start_day.strftime("%Y-%m-%d"))
        print(f"✅ Created 'day_info.txt' with start date: {start_day.strftime('%Y-%m-%d')}")
    
    with open("day_info.txt", "r") as f:
        day_info = f.read().strip()
    current_day = datetime.strptime(day_info, "%Y-%m-%d")
    while current_day < expiry_date:
        # === Load current day_info ===
        with open("day_info.txt", "r") as f:
            day_info = f.read().strip()

        current_day = datetime.strptime(day_info, "%Y-%m-%d")
    # === Stop if at expiry ===
        print("📅 Running for:", current_day.strftime("%Y-%m-%d"))
    
        # === Run the notebook ===
        pm.execute_notebook(
            "data_maker2.ipynb",
            "data_maker2_output.ipynb",
            log_output=True
        )
    
        # === Save next day to file ===
        next_day = get_next_day(day_info)
        print
        with open("day_info.txt", "w") as f:
            f.write(next_day.strftime("%Y-%m-%d"))
    
        print("➡️  Saved next day:", next_day.strftime("%Y-%m-%d"))
    print("✅ Reached expiry. Stopping.")
    return
if __name__ == "__main__":
    run_until_expiry()
