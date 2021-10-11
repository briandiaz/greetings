import threading
import time
import cv2
from core.FaceDetection import FaceDetection
from core.FaceRecognition import FaceRecognition

def main():
  video_capture = cv2.VideoCapture(0) # Initialize instance of videoCapture with Default WebCamera
  video_capture.open(0) # Open default WebCamera
  time.sleep(5) # Wait Camera to respond in 5 seconds

  detector = FaceDetection() # Initialize detector
  face_recognition = FaceRecognition()
  do_recognition = True
  # Lets create a thread to process facial recognition as it takes too much resources
  event = threading.Event()
  start_time = time.time()

  while True:
    is_read, image = video_capture.read()
    if is_read:
      # Find all faces in the image
      faces = detector.findFaces(image)
      # Draw Faces in the image
      detector.draw(faces)

      if faces and do_recognition is True:
        thread1 = threading.Thread(target=face_recognition.detect_and_greet, args=(image, event))
        thread1.start()
        start_time = time.time()

      end_time = time.time()
      time_elapsed = (end_time - start_time)
      do_recognition = time_elapsed > 5 # Start recoginition process every 5 seconds

      # Show result
      cv2.imshow("Greetings", image)
      cv2.waitKey(1)
    else:
      cv2.waitKey(1000)

    key = cv2.waitKey(30) & 0xff
    if key == 27: # When escape key is pressed video ends and opencv window is closed.
      break

  video_capture.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
  main()
