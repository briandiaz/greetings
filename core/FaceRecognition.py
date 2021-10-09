import cv2
import face_recognition
from os import listdir
from os.path import isfile, join
from core.Subject import Subject
import pyttsx3

engine = pyttsx3.init()

__ASSETS_PATH__ = './assets'

class FaceRecognition:
  def __init__(self, minDetectionConfidence=0.4) -> None:
    self.minDetectionConfidence = minDetectionConfidence
    self.subjects = self.__load_subjects__()

  def __load_subjects__(self):
    files = self.__get_files__()
    subjects = []
    
    for index, [file, name] in enumerate(files):
      filePath = join(__ASSETS_PATH__, file)
      image = face_recognition.load_image_file(filePath)
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

      faceLocation = face_recognition.face_locations(image)[0]
      faceEncoding = face_recognition.face_encodings(image)[0]
      subject = Subject(name, filePath, image, faceLocation, faceEncoding)

      subjects.append(subject)

    return subjects


  def __get_files__(self):
    files = [fileName for fileName in listdir(__ASSETS_PATH__) if isfile(join(__ASSETS_PATH__, fileName))]
    fileNameDuple = []

    for _, file in enumerate(files):
      name = file.split('.')[0]
      fileNameDuple.append([file, name])

    return fileNameDuple

  def __greet__(self, text):
    engine.say(text)
    engine.runAndWait()

  def detect_and_greet(self, image, event):
    imageTest = image
    imageTest = cv2.cvtColor(imageTest, cv2.COLOR_BGR2RGB)
    locations = face_recognition.face_locations(imageTest)
    event.wait(1)
    
    if len(locations) > 0:
      for _, subject in enumerate(self.subjects):
        encodeTest = face_recognition.face_encodings(imageTest)[0]
        results = face_recognition.compare_faces([subject.faceEncoding], encodeTest)[0]
        faceDis = face_recognition.face_distance([subject.faceEncoding], encodeTest)[0]

        if results == True and faceDis >= 0.0 and faceDis <= self.minDetectionConfidence:
          text = f'Hello {subject.name}, I can see you!'
          event.set()
          self.__greet__(text)
        else:
          text = "Intruder"

        print(text)

    