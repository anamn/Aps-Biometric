import cv2

loadAlgorithm = cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_default.xml')

image = cv2.imread('Images/image1.jpg')

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = loadAlgorithm.detectMultiScale(grayImage, scaleFactor=1.05, minNeighbors=3, minSize=(50, 50))

print(faces)

for(x, y, l, a) in faces:
    cv2.rectangle(image, (x, y), (x + l, y + a), (0, 255, 0), 2)

cv2.imshow("Faces", image)
cv2.waitKey()