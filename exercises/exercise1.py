# read, resize, rotate, display an image using opencv libarary.
import cv2

image = cv2.imread('assets/ball.png', -1)
image = cv2.resize(image, (250,250))
'''
image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('New-image.jpg', image)
'''
cv2.imshow('Windown-Name', image)
cv2.waitKey(0)
cv2.destroyAllWindows()