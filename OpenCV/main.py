import cv2

pic = cv2.imread('C:/Py/OpenCV/faces.jpg')
print(pic.shape)
pic = cv2.resize(pic, (500, 500))
print(pic.shape)
cv2.imshow('Result', pic)
cv2.waitKey(1000)