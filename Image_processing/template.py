import cv2

img = cv2.imread('C:/Users/hp/Desktop/python.py/images/image1.jpg.jpg')
template = cv2.imread('C:/Users/hp/Desktop/python.py/images/image2.jpg.jpg', 0)
result = cv2.matchTemplate(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),template, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
h, w = template.shape[:2]
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)

cv2.imshow('Detected Template', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
