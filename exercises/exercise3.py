import numpy as np
import cv2
import random

img = cv2.imread('assets/nike-ball.jpg', -1)

tag = img[150:350, 200:500]
img[0:200, 10:310] = tag
img = cv2.imshow("coping part of the image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
img = cv2.imwrite("modified_images/ball-cutted.jpg", img)
