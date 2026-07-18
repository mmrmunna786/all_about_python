# Author: Munna
# Date: 18/07/2026
import cv2

 # CascadeClassifier() loads the classifier .xml file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Check if classifier loaded correctly
if face_cascade.empty():
    print("Error: Could not load haarcascade_frontalface_default.xml")
    exit()
# Start the webcam feed  
cap = cv2.VideoCapture(0) # VideoCapture() captures the live video or still image
print("Press 'q' on your keyboard to close the webcam stream.")
while True:
    # 1. Capture frame-by-frame inside the loop
    res, img = cap.read() # read() will return true or false and the image coordinates
    if not res:
        print("Error: Failed to grab frame from webcam.")
        break
    # 2. convert to grayscale for detection
    gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY ) # cvtColor() converts a rgb image to grayscale image
    # 3. Detect faces on the current frame
    faces = face_cascade.detectMultiScale( gray, 1.3, 5 )
	# print( res, "\n", img ) 
	# 4. Draw bounding boxes
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2) # to draw a rectangle on the face
	# 5. Display the resulting frame live
    cv2.imshow( "Real-Time Face Detection", img )
    # 6. Break the loop if the 'q' key is pressed
    # cv2.waitKey(1) checks for input every 1 millisecond instead of pausing indefinitely
    if cv2.waitKey(1) == ord('q'):
        break
# Clean up and close down
cap.release()
cv2.destroyAllWindows()
