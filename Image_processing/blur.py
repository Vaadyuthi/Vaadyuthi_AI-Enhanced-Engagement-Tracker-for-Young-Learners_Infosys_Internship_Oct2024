import cv2

img = cv2.imread('C:/Users/hp/Desktop/python.py/images/image1.jpg.jpg')
blur = cv2.GaussianBlur(img, (15, 15), 0)

cv2.imshow('Blurred Image', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()