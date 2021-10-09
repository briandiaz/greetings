import cv2
import mediapipe as mp
from core.Face import Face

class FaceDetection():
  def __init__(self, minDetectionConfidence=0.5):
    self.minDetectionConfidence = minDetectionConfidence
    self.faceDetection = mp.solutions.face_detection.FaceDetection(self.minDetectionConfidence)

  def findFaces(self, image):
    self.image = image
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    detectionProcess = self.faceDetection.process(imageRGB)
    faces = []

    if detectionProcess.detections:
      for index, detection in enumerate(detectionProcess.detections):
        boundingBoxLocation = detection.location_data.relative_bounding_box
        imageHeight, imageWidth, _ = image.shape

        if boundingBoxLocation.xmin > 0:
          boundingBox = int(boundingBoxLocation.xmin * imageWidth), int(boundingBoxLocation.ymin * imageHeight), \
                int(boundingBoxLocation.width * imageWidth), int(boundingBoxLocation.height * imageHeight)
          face = Face(index + 1, detection.score[0], boundingBox)

          faces.append(face)

    return faces

  def draw(self, faces):
    lineWidth = 3

    for _, face in enumerate(faces):
      x, y, w, h = face.boundingBox
      x1, y1 = x + w, y + h
      cv2.rectangle(self.image, (x1, y), (x, y1), (255, 0, 255), lineWidth)
 