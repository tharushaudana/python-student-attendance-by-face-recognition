import system.students as students
import system.capturing as capturing
from mark_attendance import mark_attendance
from mark_attendance import init_today

def on_face(st_id):
    data = students.get(st_id)

    if (data == None): return "Unknown"

    if (not students.is_attempted(st_id)):
        mark_attendance(st_id, data)
        students.mark_attempted(st_id)

    return data['name']

students.load()

init_today(students.students)

capturing.init()
capturing.run(on_face)
capturing.close()