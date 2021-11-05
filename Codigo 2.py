import cv2
import numpy as np



image = cv2.imread('Images/image7.jpg')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = loadFace.detectMultiScale(grayImage)

for(x, y, l, a) in faces:
    data = cv2.rectangle(image, (x, y), (x + l, y + a), (255, 0, 255), 2)
    eyeArea = data[y:y + a, x:x + l]
    grayEyeArea = cv2.cvtColor(eyeArea, cv2.COLOR_BGR2GRAY)
    detected = loadEye.detectMultiScale(grayEyeArea, scaleFactor=1.3, minNeighbors = 9)

    for(ox, oy, ol, oa) in detected:
        cv2.rectangle(eyeArea, (ox, oy), (ox + ol, oy + oa), (0, 255, 255), 2)

np_array = np.array(image)

rgb = np_array[:, :, ::-1]

rects = detected

print(rects)

cv2.imshow("Eye detection", image)
cv2.waitKey()