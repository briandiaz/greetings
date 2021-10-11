from os import listdir
from os.path import isfile, join
import cv2
import face_recognition
import pyttsx3
from core.Subject import Subject

engine = pyttsx3.init()

__ASSETS_PATH__ = './assets'

class FaceRecognition:
  def __init__(self, min_detection_confidence=0.4) -> None:
    self.min_detection_confidence = min_detection_confidence
    self.subjects = self.__load_subjects__()

  def __load_subjects__(self):
    files = self.__get_files__()
    subjects = []
    
    for _, [file, name] in enumerate(files):
      file_path = join(__ASSETS_PATH__, file)
      image = face_recognition.load_image_file(file_path)
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

      face_location = face_recognition.face_locations(image)[0]
      face_encoding = face_recognition.face_encodings(image)[0]
      subject = Subject(name, file_path, image, face_location, face_encoding)

      subjects.append(subject)

    return subjects


  def __get_files__(self):
    files = [fileName for fileName in listdir(__ASSETS_PATH__) if isfile(join(__ASSETS_PATH__, fileName))]
    file_name_duple_list = []

    for _, file in enumerate(files):
      name = file.split('.')[0]
      file_name_duple_list.append([file, name])

    return file_name_duple_list

  def __greet__(self, text):
    engine.say(text)
    engine.runAndWait()

  def detect_and_greet(self, image, event):
    image_test = image
    image_test = cv2.cvtColor(image_test, cv2.COLOR_BGR2RGB)
    locations = face_recognition.face_locations(image_test)
    event.wait(1)

    if len(locations) > 0:
      for _, subject in enumerate(self.subjects):
        encode_test = face_recognition.face_encodings(image_test)[0]
        results = face_recognition.compare_faces([subject.face_encoding], encode_test)[0]
        face_distance = face_recognition.face_distance([subject.face_encoding], encode_test)[0]

        if results == True and face_distance >= 0.0 and \
          face_distance <= self.min_detection_confidence:
          text = f'Hello {subject.name}, I can see you!'
          event.set()
          self.__greet__(text)
        else:
          text = "Intruder"

        print(text)
