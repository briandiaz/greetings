import cv2
import time
from core.FaceDetection import FaceDetection
from core.FaceRecognition import FaceRecognition
import threading

def main():
  video_capture = cv2.VideoCapture(0) # Initialize instance of videoCapture with Default WebCamera
  video_capture.open(0) # Open default WebCamera
  time.sleep(5) # Wait Camera to respond in 5 seconds

  detector = FaceDetection() # Initialize detector
  faceRecognition = FaceRecognition()
  doRecognition = True
  event = threading.Event() # Lets create a thread to process facial recognition as it takes too much resources
  startTime = time.time()

  while True:
    is_read, image = video_capture.read()
    if is_read:
      # Find all faces in the image
      faces = detector.findFaces(image)
      # Draw Faces in the image
      detector.draw(faces)

      if faces and doRecognition == True:
        thread1 = threading.Thread(target=faceRecognition.detect_and_greet, args=(image, event))
        thread1.start()
        startTime = time.time()

      endTime = time.time()
      timeElapsed = (endTime - startTime)
      doRecognition = timeElapsed > 5 # Start recoginition process every 5 seconds

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