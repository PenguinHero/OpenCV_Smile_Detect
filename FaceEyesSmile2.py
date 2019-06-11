# This version uses the SenseHat to display status.
# Solid Blue is running.
# Solid Green is Face detected
# Green Smile is smile detected.

import cv2

from sense_hat import SenseHat
import time

sense = SenseHat()

# PRESS ESCAPE KEY WHEN RUNNING TO EXIT THE PROGRAM.

# Set up pixel images.

r = [255, 0, 0]
o = [255, 127, 0]
y = [255, 255, 0]
g = [0, 255,0]
b = [0, 0, 255]
i = [75, 0, 130]
v = [159, 0, 255]
e = [0,0,0]

smile_image = [ e,e,e,e,e,e,e,e,
                e,e,e,e,e,e,e,e,
                e,g,e,e,e,e,e,g,
                e,g,e,e,e,e,e,g,
                e,e,g,e,e,e,g,e,
                e,e,e,g,g,g,e,e,
                e,e,e,e,e,e,e,e,
                e,e,e,e,e,e,e,e ]

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')


cap = cv2.VideoCapture(0)

while True:
    
    sense.clear(0,0,255)  # Set to Blue
    
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    ###Face detection
    
    if len(faces) > 0:
        sense.clear(0,255,0) # Set to Green
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        ###smile detection

# original smile parameters
#        smile = smile_cascade.detectMultiScale(
#            roi_gray,
#            scaleFactor=1.7,
#            minNeighbors=22,
#            minSize=(25, 25),
#            flags=cv2.CASCADE_SCALE_IMAGE
#        )
        smile = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor= 1.16,
            minNeighbors=35,
            minSize=(25, 25),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        ##Eye Detection
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            print ("Found eyes: " + str(len(eyes)))

        # Set region of interest for smiles
                
        for (x, y, w, h) in smile:
            print ("***** Found smile: " + str(len(smile)))
            cv2.rectangle(roi_color, (x, y), (x + w, y + h), (0, 0, 255), 1)

        if len(smile) > 0:
            sense.set_pixels(smile_image)  # Show smile
            time.sleep(0.5)                # hopefully sleeping half a second soes upset CV cycle...

    cv2.imshow('Face', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

sense.clear(0,0,0)