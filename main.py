import system.capturing as capturing

def on_face(face_id):
    return face_id

capturing.init()

capturing.run(on_face)

capturing.close()