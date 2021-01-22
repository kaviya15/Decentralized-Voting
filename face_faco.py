import face_recognition
import cv2
import numpy as np
from data_load import  *
video_capture = cv2.VideoCapture(0)
name = ""
# imgkaviya = face_recognition.load_image_file('images/kaviya.jpg')
# imgkaviya_encoding = face_recognition.face_encodings(imgkaviya)[0]
# imgsm= face_recognition.load_image_file('images/sm.png')
# imgsm_encoding = face_recognition.face_encodings(imgsm)[0]
# imgramya = face_recognition.load_image_file('images/ramya.jpg')
# imgramya_encoding = face_recognition.face_encodings(imgramya)[0]
# imgjeni= face_recognition.load_image_file('images/jenisha.jpg')
# imgjeni_encoding = face_recognition.face_encodings(imgjeni)[0]
# imgnisha= face_recognition.load_image_file('images/NISHA.jpg')
# imgnisha_encoding = face_recognition.face_encodings(imgnisha)[0]
# imgdp= face_recognition.load_image_file('images/dp.jpeg')
# imgdp_encoding = face_recognition.face_encodings(imgdp)[0]
# # Create arrays of known face encodings and their names
# known_face_encodings = [
#     imgkaviya_encoding,
#     imgsm_encoding,
#     imgramya_encoding,
#     imgjeni_encoding,
#     imgnisha_encoding ,
#     imgdp_encoding
#
# ]
# known_face_names = [
#     "kaviya",
#     "sm",
#     "ramya",
#     "jeni",
#     "nisha",
#     "dp"
# ]
# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)
    process_this_frame = not process_this_frame
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    # Display the resulting image
    cv2.imshow('Video', frame)
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

def check_eligible():
    return name
