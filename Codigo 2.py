import cv2

loadFace = cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_default.xml')
loadEye = cv2.CascadeClassifier('Haarcascade/haarcascade_eye.xml')

image = cv2.imread('Images/image8.jpg')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = loadFace.detectMultiScale(grayImage)

for(x, y, l, a) in faces:
    data = cv2.rectangle(image, (x, y), (x + l, y + a), (0, 255, 0), 2)
    eyeArea = data[y:y + a, x:x + l]
    grayEyeArea = cv2.cvtColor(eyeArea, cv2.COLOR_BGR2GRAY)
    detected = loadEye.detectMultiScale(grayEyeArea, scaleFactor=1.3, minNeighbors = 9)

    for(ox, oy, ol, oa) in detected:
        cv2.rectangle(eyeArea, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)

cv2.imshow("Eye detection", image)
cv2.waitKey()