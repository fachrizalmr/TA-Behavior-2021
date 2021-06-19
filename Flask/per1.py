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
idrelay = [1, 2, 3, 4]


def preprocessingData(w, h, ir):
    data = pd.read_csv('FixData.csv')
    data = pd.DataFrame(data, columns=['waktu', 'hari', 'idrelay', 'status'])
    x = data.iloc[:, 0:3].values
    y = data.iloc[:, -1].values
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=0)
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.fit_transform(x_test)
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(units=3, activation='relu'))
    model.add(tf.keras.layers.Dense(units=375, activation='relu'))
    model.add(tf.keras.layers.Dense(units=2, activation='softmax'))
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=1150, batch_size=128)
    xData = model.evaluate(x_test, y_test, batch_size=128)
    df = pd.DataFrame({'waktu': [w], 'hari': [h], 'idrelay': [ir]})
    dataf = df.values
    dataf = sc.fit_transform(dataf)
    predict = model.predict(dataf)

    yData = np.argmax(predict)
    akurasi = float(xData[1])
    status = int(yData)

    return status, akurasi


def proses_kirim():
    for i in range(4):
        data_preprocessing = preprocessingData(waktu, hari, idrelay[i])
        print(waktu, hari, idrelay[i],
              data_preprocessing[0], data_preprocessing[1])
        head = 'relay'
        head += str(i+1)
        db.child("behavior").child(head).update(
            {"waktu": waktu, "hari": hari, "idrelay": idrelay[i], "status": data_preprocessing[0], "akurasi": data_preprocessing[1]})


while True:
    proses_kirim()
