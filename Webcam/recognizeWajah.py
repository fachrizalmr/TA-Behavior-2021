import cv2
import os
wajahDir = 'dataWajah'
latihDir = 'latihWajah'
cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faceRecognizer = cv2.face.LBPHFaceRecognizer_create()

faceRecognizer.read(latihDir+'/training.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

id = 0
names = ['0', 'Fachrizal', 'Gaben']
minWidth = 0.1*cam.get(3)
minHeight = 0.1*cam.get(4)

while True:
    retV, frame = cam.read()
    frame = cv2.flip(frame, 1)  # vertical flip
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(
        grey, 1.2, 5, minSize=(round(minWidth), round(minHeight)),)
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        id, confidence = faceRecognizer.predict(grey[y:y+h, x:x+w])
        if confidence <= 50:
            nameID = names[id]
            confidenceTxt = " {0}%".format(round(100-confidence))
        else:
            nameID = names[0]
            confidenceTxt = " {0}%".format(round(100-confidence))
        cv2.putText(frame, str(nameID), (x+5, y-5),
                    font, 1, (255, 255, 255), 2)
        cv2.putText(frame, str(confidenceTxt), (x+5, y+h-5),
                    font, 1, (255, 255, 0), 1)

    cv2.imshow('Recognisi Wajah', frame)
    k = cv2.waitKey(1) & 0xFF == ord('q')
    if k == 27 or k == ord('q'):
        break
print("Exit")
cam.release()
cv2.destroyAllWindows()
