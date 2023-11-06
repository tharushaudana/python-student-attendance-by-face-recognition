from datetime import datetime
import attendsheet as ast

today = None

def init_today(students):
    global today

    today = datetime.now().strftime("%Y-%b-%d")

    ast.create_dir_if_not_exists()
    ast.create_wb_for_today(students, today)

def mark_attendance(st_id, data):
    time = datetime.now().strftime("%H:%M:%S")

    print("New attempt", today, time, st_id, data)
    
    ast.mark_attempt(st_id, data['class'], time)
