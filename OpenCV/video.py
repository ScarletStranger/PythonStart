import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# img = cv2.imread('C:\\Py\\OpenCV\\unnamed.jpg')
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# faces = face_cascade.detectMultiScale(img_gray)

# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# cv2.imshow('Result', img)
# cv2.waitKey(0)

cap = cv2.VideoCapture('C:\Py\OpenCV\Warhammer.mp4')

while True:
    success, frame = cap.read()
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imshow('Result', frame)

    if cv2.waitKey(30) & 0xff == ord('q'):
        break
