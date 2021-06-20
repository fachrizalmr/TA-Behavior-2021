import tensorflow as tf
import numpy as np
import pandas as pd
import time
from datetime import datetime
from datetime import date
import schedule
import pyrebase
import waktu as wk
import json
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.python.eager.context import num_gpus
from os import read, stat_result
from re import T, X

config = {
    "apiKey": "AIzaSyAUXrAk1Z_8kRa3NH1czDXUE5xPTP-gJ_Y",
    "authDomain": "cloudta2021-fa4af.firebaseapp.com",
    "databaseURL": "https://cloudta2021-fa4af-default-rtdb.firebaseio.com",
    "storageBucket": "cloudta2021-fa4af.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
timeNow = datetime.now()
jam = timeNow.hour
menit = timeNow.minute
timestamp = timeNow.strftime("%H:%M")


def cekHari():
    cekNow = date.today().strftime("%A")
    if cekNow == 'Monday':
        now = 1

    elif cekNow == 'Tuesday':
        now = 2

    elif cekNow == 'Wednesday':
        now = 3

    elif cekNow == 'Thursday':
        now = 4

    elif cekNow == 'Friday':
        now = 5

    elif cekNow == 'Saturday':
        now = 6

    elif cekNow == 'Sunday':
        now = 7

    return now


waktu = wk.cekWaktu(jam, menit)
hari = cekHari()
day = date.today().strftime("%A")
idrelay = [1, 2, 3, 4]


def preprocessingData(w, h):
    data = pd.read_csv('FixData.csv')
    data = pd.DataFrame(data, columns=['waktu', 'hari', 'idrelay', 'status'])
    x = data.iloc[:, 0:3].values
    y = data.iloc[:, -1].values
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.1, random_state=0)
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.fit_transform(x_test)
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(units=3, activation='relu'))
    model.add(tf.keras.layers.Dense(units=28, activation='relu'))
    model.add(tf.keras.layers.Dense(units=2, activation='sigmoid'))
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=750, batch_size=128)
    xData = model.evaluate(x_test, y_test, batch_size=128)
    df = pd.DataFrame({'waktu': [w, w, w, w], 'hari': [
                      h, h, h, h], 'idrelay': [1, 2, 3, 4]})
    dataf = df.values
    dataf = sc.fit_transform(dataf)
    predict = model.predict(dataf)
    akurasi = float(xData[1])

    arr_pred = []
    for i in range(len(predict)):
        arr_pred.append(np.argmax(predict[i]))
        print(w, h, idrelay[i], arr_pred[i], "Nilai Akurasi = ", akurasi)
        convert = int(arr_pred[i])
        if convert == 0:
            convert = "OFF"
        else:
            convert = "ON"
        head = 'relay'
        head += str(i+1)
        db.child("Relay4Channel").child("behavior").child(head).update(
            {"waktu": str(timestamp), "interval": w, "hari": str(day), "idrelay": idrelay[i], "status": convert})

    db.child("Relay4Channel").child("behavior").update({"akurasi": akurasi})

    return akurasi


while True:
    preprocessingData(waktu, hari)
