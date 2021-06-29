import cv2
import os
wajahDir = 'dataWajah'
cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeDetector = cv2.CascadeClassifier('haarcascade_eye.xml')
faceID = input(
    "Masukkan Face ID yang akan di rekam Dataya [Kemudian Tekan Enter]: ")
print("Tatap wajah ke depan Anda ke dalam webcam. Tunggu proses pengambilan data wajah selesai.")
ambilData = 1
while True:
    retV, frame = cam.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(grey, 1.3, 5)
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        namaFile = 'wajah.'+str(faceID)+'.'+str(ambilData)+'.jpg'
        cv2.imwrite(wajahDir+'/'+namaFile, frame)
        ambilData += 1
        roigrey = grey[y:y+h, x:x+w]
        roiWarna = frame[y:y+h, x:x+w]
        eyes = eyeDetector.detectMultiScale(roigrey)
        for (xe, ye, we, he) in eyes:
            cv2.rectangle(roiWarna, (xe, ye), (xe+we, ye+he), (0, 0, 255), 1)

    cv2.imshow('MyWebcam', frame)
    k = cv2.waitKey(1) & 0xFF == ord('q')
    if k == 27 or k == ord('q'):
        break
    elif ambilData > 30:
        break
print("Pengambilan Data Selesai")
cam.release()
cv2.destroyAllWindows()
