import cv2

img = cv2.imread('C:/Users/hp/Desktop/python.py/images/image1.jpg.jpg')
resized = cv2.resize(img, (300 , 300))

cv2.imshow('Resized Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

