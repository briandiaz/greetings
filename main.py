import cv2
import time
 
video_capture = cv2.VideoCapture(0) # Initialize instance of videoCapture with Default WebCamera
video_capture.open(0) # Open default WebCamera
time.sleep(5) # Wait Camera to respond in 5 seconds

def main():
  while True:
    is_read, image = video_capture.read()
    if is_read:
      cv2.imshow("Greetings", image)

    key = cv2.waitKey(30) & 0xff
    if key == 27: # If escape key is pressed video ends and opencv window is closed.
      break
  
  video_capture.release()
  cv2.destroyAllWindows()

 
 
if __name__ == "__main__":
  main()