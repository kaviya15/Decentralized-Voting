import face_recognition
import os
def load_img(file):
     img = face_recognition.load_image_file(file)
     img_encoding = face_recognition.face_encodings(img)[0]
     return img_encoding
base_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(base_dir,"images")
ls=[ file for root,dir,files in os.walk(image_dir) for file in files]
known_face_names = [j.split('.')[0] for j in ls ]
print(known_face_names)
known_face_encodings = [load_img('images/'+file)  for root,dir,files in os.walk(image_dir) for file in files]
print(known_face_encodings)
