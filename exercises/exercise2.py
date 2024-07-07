# Image Fundemental and manuplation
import cv2
import numpy as np
import random

image = cv2.imread('modified_images/saved_image.png', -1)

for i in range(100):
    for j in range(image.shape[1]):

        #image[i][j] = [0,255,250]
        image[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imshow("my-window", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
