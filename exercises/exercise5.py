# Drawing (line, images, circle, text)
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    '''
        (0,0)  ----------> x axix
          |
          |      coordinating sys in cv libararies
          |
          V
        y axix

    '''
    img = cv2.line(frame, (0,0), (width, height), (255,0,0), 10)
    img = cv2.line(img, (0,height), (width, 0), (0,255,0), 5)
    img = cv2.rectangle(img, (150,150), (300,300), (128,128,128), 4)
    img = cv2.rectangle(img, (20,20), (150,150), (190,190,121), -1)
    img = cv2.circle(img, (350,350), 60, (0,0,255), -1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Qusay is great!', (10, height - 10), font, 1, (0,0,0), 5, cv2.LINE_AA)
                                               # coordinates stars from botton left corner


    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()