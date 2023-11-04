import cv2
import config as config
from system.simple_facerec import SimpleFacerec
from datetime import datetime

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images(config.images_path)

cap = None

def close():
    if (cap == None): return
    cap.release()
    cv2.destroyAllWindows()

def get_datetime_str():
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

def pre_process_frame(frame):
    #frame = cv2.resize(frame,(640, 480));
    cv2.rectangle(frame, (0, 0), (380, 100), (200, 200, 200), -1)
    cv2.putText(frame, "STUDENT ATTENDENCE", (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 200), 4)
    cv2.putText(frame, get_datetime_str(), (10, 80), cv2.FONT_HERSHEY_PLAIN, 1, (200, 0, 0), 2)
    return frame

def detect_face(frame):
    # Detect Faces
    face_locations, face_ids = sfr.detect_known_faces(frame)
    return face_locations, face_ids

def mark_on_face(frame, face_loc, name):
    y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

    cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

def init():
    global cap

    # Load Camera
    cap = cv2.VideoCapture(config.video_device_index)

    if (not cap.isOpened()):
        print("Unable to start video capture.")
        close()
        exit()

def run(cb):
    while (True):
        ret, frame = cap.read()

        frame = pre_process_frame(frame)

        face_locations, face_ids = detect_face(frame)

        for face_loc, face_id in zip(face_locations, face_ids):
            mark_on_face(frame, face_loc, cb(face_id))

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)

        if (key == 27):
            break