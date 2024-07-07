# Template Matching (Object Detectioin)
import numpy as np
import cv2

img = cv2.imread('assets/soccer_practise.jpg', 0) # detecting the ball
# img = cv2.resize(cv2.imread('assets/soccer_practise.jpg', 0), (0, 0), fx=0.8, fy=0.8) 
template = cv2.imread('assets/seg1.jpg', 0) # ball
# template = cv2.resize(cv2.imread('assets/seg2.jpg', 0), (0, 0), fx=0.8, fy=0.8)


height, width = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + width, location[1] + height)
    cv2.rectangle(img2, location, bottom_right, 255, 5)

    cv2.imwrite('modified_images/seg1.jpg', img2)
    cv2.imshow('match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




