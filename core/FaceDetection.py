import cv2
import mediapipe as mp
from core.Face import Face

class FaceDetection():
  def __init__(self, min_detection_confidence=0.5):
    self.min_detection_confidence = min_detection_confidence
    self.face_detection = mp.solutions.face_detection.FaceDetection(self.min_detection_confidence)
    self.image = None

  def find_faces(self, image):
    self.image = image
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    detection_process = self.face_detection.process(image_rgb)
    faces = []

    if detection_process.detections:
      for index, detection in enumerate(detection_process.detections):
        bounding_box_location = detection.location_data.relative_bounding_box
        image_height, image_width, _ = image.shape

        if bounding_box_location.xmin > 0:
          bounding_box = int(bounding_box_location.xmin * image_width), int(bounding_box_location.ymin * image_height), \
                int(bounding_box_location.width * image_width), int(bounding_box_location.height * image_height)
          face = Face(index + 1, detection.score[0], bounding_box)

          faces.append(face)

    return faces

  def draw(self, faces):
    line_width = 3

    for _, face in enumerate(faces):
      x_pos, y_pos, width, heigth = face.bounding_box
      x1_pos, y1_pos = x_pos + width, y_pos + heigth
      cv2.rectangle(self.image, (x1_pos, y_pos), (x_pos, y1_pos), (255, 0, 255), line_width)
 