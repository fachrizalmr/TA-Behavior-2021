from tensorflow.python.ops.functional_ops import While
import tensorflow as tf
import numpy as np
import pandas as pd
import waktu as wk
import time
from datetime import datetime
from datetime import date
import schedule
import pyrebase
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tensorflow import keras
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.python.eager.context import num_gpus
from os import read, stat_result
from re import T, X

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

dbStore = firestore.client()


def cekHari():
    cekNow = date.today().strftime("%A")
    if cekNow == 'Monday':
        now = 0

    elif cekNow == 'Tuesday':
        now = 1

    elif cekNow == 'Wednesday':
        now = 2

    elif cekNow == 'Thursday':
        now = 3

    elif cekNow == 'Friday':
        now = 4

    elif cekNow == 'Saturday':
        now = 5

    elif cekNow == 'Sunday':
        now = 6

    return now


config = {
    "apiKey": "AIzaSyAUXrAk1Z_8kRa3NH1czDXUE5xPTP-gJ_Y",
    "authDomain": "cloudta2021-fa4af.firebaseapp.com",
    "databaseURL": "https://cloudta2021-fa4af-default-rtdb.firebaseio.com",
    "storageBucket": "cloudta2021-fa4af.appspot.com"
}

DataHead = "Dataset Hasil Pengujian"
firebase = pyrebase.initialize_app(config)
db = firebase.database()
timeNow = datetime.now()
jam = timeNow.hour
menit = timeNow.minute
timestamp = timeNow.strftime("%H:%M")
day = date.today().strftime("%A")
idrelay = [0, 1, 2, 3]
hari = cekHari()
waktu = wk.cekWaktu(jam, menit)
data = pd.read_csv('FixDataBind.csv')
data = pd.DataFrame(data, columns=['waktu', 'hari', 'idrelay', 'status'])
data['waktu'] = pd.factorize(data['waktu'])[0]
data['hari'] = pd.factorize(data['hari'])[0]
data['idrelay'] = pd.factorize(data['idrelay'])[0]
data['status'] = pd.factorize(data['status'])[0]
x = data.iloc[:, 0:3].values
y = data.iloc[:, -1].values
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.1, random_state=0)
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=3, activation='relu'))
model.add(tf.keras.layers.Dense(units=26, activation='relu'))
model.add(tf.keras.layers.Dense(units=8, activation='relu'))
model.add(tf.keras.layers.Dense(units=2, activation='sigmoid'))
start = time.perf_counter()
opt = keras.optimizers.Adam(learning_rate=0.01)
model.compile(optimizer=opt,
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=500, batch_size=128)

print(model.layers[0].weights)
# print(model.layers[0].bias.numpy())
print(model.layers[1].weights)
# print(model.layers[1].bias.numpy())
print(model.layers[2].weights)
# print(model.layers[2].bias.numpy())
print(model.layers[3].weights)
# print(model.layers[3].bias.numpy())
xData = model.evaluate(x_test, y_test, batch_size=128)
elapsed = time.perf_counter() - start
akurasi = float(xData[1])
error = float(xData[0])
df = pd.read_csv('FixDataBind.csv')
df['waktu'] = pd.factorize(df['waktu'])[0]
df['hari'] = pd.factorize(df['hari'])[0]
df['idrelay'] = pd.factorize(df['idrelay'])[0]
df['status'] = pd.factorize(df['status'])[0]
df = df.drop(['status'], axis=1)
dataf = df.values
dataf = sc.fit_transform(dataf)
predict = model.predict(dataf)

arr_pred = []
for i in range(len(predict)):
    arr_pred.append(np.argmax(predict[i]))

df['prediksi'] = arr_pred


db.child("Relay4Channel").child("behavior").update(
    {"akurasi": akurasi, "loss": error, "waktu": str(timestamp), "hari": str(day)})


def reportR1():
    output = []
    output = df[(df['waktu'] == waktu) & (
        df['hari'] == hari) & (df['idrelay'] == 0)]

    idRelay = output.iloc[0]['idrelay']
    sRelay = output.iloc[0]['prediksi']
    if sRelay == 1:
        statusRelay = "ON"
    else:
        statusRelay = "OFF"

    db.child("Relay4Channel").child("behavior").child("relay1").update({"waktu": str(
        timestamp), "interval": int(waktu), "hari": str(day), "idrelay": int(idRelay), "status": str(statusRelay)})

    data = {'status': str(statusRelay), 'idrelay': int(idRelay),
            'akurasi': akurasi, 'loss': error, 'interval': int(waktu)}

    dbStore.collection(DataHead).document(str(day + " " + datetime.today().strftime('%d-%m-%Y'))
                                          ).collection("pengguna1").document(str(timestamp)).set(data)

    print(output)


def reportR2():
    output = []
    output = df[(df['waktu'] == waktu) & (
        df['hari'] == hari) & (df['idrelay'] == 1)]

    idRelay = output.iloc[0]['idrelay']
    sRelay = output.iloc[0]['prediksi']
    if sRelay == 1:
        statusRelay = "ON"
    else:
        statusRelay = "OFF"

    db.child("Relay4Channel").child("behavior").child("relay2").update({"waktu": str(
        timestamp), "interval": int(waktu), "hari": str(day), "idrelay": int(idRelay), "status": str(statusRelay)})

    data = {'status': str(statusRelay), 'idrelay': int(idRelay),
            'akurasi': akurasi, 'loss': error, 'interval': int(waktu)}

    dbStore.collection(DataHead).document(str(day + " " + datetime.today().strftime('%d-%m-%Y'))
                                          ).collection("pengguna2").document(str(timestamp)).set(data)

    print(output)


def reportR3():
    output = []
    output = df[(df['waktu'] == waktu) & (
        df['hari'] == hari) & (df['idrelay'] == 2)]

    idRelay = output.iloc[0]['idrelay']
    sRelay = output.iloc[0]['prediksi']
    if sRelay == 1:
        statusRelay = "ON"
    else:
        statusRelay = "OFF"

    db.child("Relay4Channel").child("behavior").child("relay3").update({"waktu": str(
        timestamp), "interval": int(waktu), "hari": str(day), "idrelay": int(idRelay), "status": str(statusRelay)})

    data = {'status': str(statusRelay), 'idrelay': int(idRelay),
            'akurasi': akurasi, 'loss': error, 'interval': int(waktu)}

    dbStore.collection(DataHead).document(str(day + " " + datetime.today().strftime('%d-%m-%Y'))
                                          ).collection("pengguna3").document(str(timestamp)).set(data)

    print(output)


def reportR4():
    output = []
    output = df[(df['waktu'] == waktu) & (
        df['hari'] == hari) & (df['idrelay'] == 3)]

    idRelay = output.iloc[0]['idrelay']
    sRelay = output.iloc[0]['prediksi']
    if sRelay == 1:
        statusRelay = "ON"
    else:
        statusRelay = "OFF"

    db.child("Relay4Channel").child("behavior").child("relay4").update({"waktu": str(
        timestamp), "interval": int(waktu), "hari": str(day), "idrelay": int(idRelay), "status": str(statusRelay)})

    data = {'status': str(statusRelay), 'idrelay': int(idRelay),
            'akurasi': akurasi, 'loss': error, 'interval': int(waktu)}

    dbStore.collection(DataHead).document(str(day + " " + datetime.today().strftime('%d-%m-%Y'))
                                          ).collection("pengguna4").document(str(timestamp)).set(data)

    print(output)


reportR1()
reportR2()
reportR3()
reportR4()

print('Elapsed %.3f seconds.' % elapsed)
print("Hari : ", str(day))
print("Interval : ", waktu)
print("Waktu : ", str(timestamp))
print("Akurasi : ", akurasi)
print("Loss/Error : ", error)
print(confusion_matrix(y, arr_pred))
print(classification_report(y, arr_pred))
