# corner detection
import numpy as np
import cv2

path = 'assets/chessboard.png'
img = cv2.imread(path)
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
''' some algorithm works well on greyscale images,
        so most times we have to convert it to greyscale before applying any changes
    '''
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
''' Shi-Tomasi Corner Detector & Good Feature to Track -> algorithm to detect corner
'''
corners = cv2.goodFeaturesToTrack(gray_img, 150, 0.01, 10) # image quality level btw 0-1 
''' 10 at the last is for Euclidean distance
    simple way to calculate it
    if we have (x1, y1) (x2, y2)
    sqrt((x2 = x1)^2 + (y2 - y1)^2)
'''
# print(corners) -> result is floating values, must change to int
corners = np.intp(corners)
for corner in corners:
    x, y = corner.ravel() # this will flatten the image. ex [[[1,2,3]]] -> [1,2,3], [[1,2],[2,1]] -> [1,2,2,1]
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
    
for i in range (len(corners)):
    for j in range (i+1, len(corners)):

        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0,255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)


cv2.imwrite('modified_images/chessboard_lines.png', img)
cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
