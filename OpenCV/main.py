import cv2

pic = cv2.imread('faces.jpg')
print(pic.shape)
pic = cv2.resize(pic, (500, 500))
print(pic.shape)
