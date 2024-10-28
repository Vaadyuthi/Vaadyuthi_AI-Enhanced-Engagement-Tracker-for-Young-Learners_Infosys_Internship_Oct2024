import cv2

img = cv2.imread('C:/Users/hp/Desktop/python.py/images/image2.jpg.jpg', 0)
equalized = cv2.equalizeHist(img)

cv2.imshow('Equalized Image', equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()