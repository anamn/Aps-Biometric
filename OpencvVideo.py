import cv2
import numpy as np

webCamera = cv2.VideoCapture(0)
loadFace = cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_default.xml')
loadEye = cv2.CascadeClassifier('Haarcascade/haarcascade_eye.xml')
loadMouth = cv2.CascadeClassifier('Haarcascade/haarcascade_smile.xml')

while True:
    camera, frame = webCamera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = loadFace.detectMultiScale(gray)

    for (x, y, l, a) in faces:
        data = cv2.rectangle(frame, (x, y), (x + l, y + a), (255, 0, 255), 2)
        area = data[y:y + a, x:x + l]
        grayArea = cv2.cvtColor(area, cv2.COLOR_BGR2GRAY)
        detectedEye = loadEye.detectMultiScale(grayArea, scaleFactor=1.3, minNeighbors=9)
        detectedMouth = loadMouth.detectMultiScale(grayArea, scaleFactor=1.3, minNeighbors=9)

        for (ox, oy, ol, oa) in detectedEye:
            cv2.rectangle(area, (ox, oy), (ox + ol, oy + oa), (0, 255, 255), 2)

        for (ox, oy, ol, oa) in detectedMouth:
            cv2.rectangle(area, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)


    cv2.imshow("Video WebCamera", frame)
    if cv2.waitKey(1) == ord('f'):
        break

np_array = np.array(frame)
rgb = np_array[:, :, ::-1]
rects = faces
print(rects)

if not rects:
    print('Nenhuma face encontrada na imagem!')

else:
    encodings = np.array(rgb)
    print ()

webCamera.release()
cv2.destroyAllWindows()