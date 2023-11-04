from datetime import datetime

def mark_attendance(st_id, data):
    today = datetime.now().strftime("%b-%d-%Y")
    time = datetime.now().strftime("%H:%M:%S")

    print("New attempt", today, time, st_id, data)
