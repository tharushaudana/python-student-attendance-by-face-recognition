# Live Student Attendance by Face Recognition

This project facilitates live student attendance using face recognition technology.

## Features

- Real-time face recognition with visual student identification via drawn rectangles.
- Graphical User Interface (GUI).
- Automatic creation of daily Excel files for attendance records.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/tharushaudana/python-student-attendance-by-face-recognition.git
   ```

2. Install dependencies from `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```

## Instructions

1. **Clone the Repository**

2. **Configure Parameters in `config.py`**

   Modify the following parameters in `config.py` if needed:
   ```python
   video_device_index = 0
   images_path = 'assets/student_images/'
   student_data_path = 'assets/student_data.xlsx'
   attendsheets_dir_path = 'Attend Sheets/'
   ```

3. **Create `student_data.xlsx`**

   Create `student_data.xlsx` in `assets/student_data.xlsx` with student information. Refer to ![student_data.png](screenshots/student_data.png) for the required format.

4. **Store Student Images**

   Store student images in `assets/student_images/`, ensuring filenames correspond to student IDs in `student_data.xlsx`. See ![student_images.png](screenshots/student_images.png) for an example.

5. **Attendance Sheets**

   Attendance sheets are automatically generated daily in `Attend Sheets/`. View ![attend_sheets.png](screenshots/attend_sheets.png) for an example and ![attend_sheet_sample.png](screenshots/attend_sheet_sample.png) for a sample attendance sheet.

6. **Sample Video**

   Watch a demonstration of live recognition in ![sample.mp4](screenrecordings/sample.mp4).

---

We hope this project proves valuable to you!
