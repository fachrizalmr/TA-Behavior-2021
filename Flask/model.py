from os import read
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def preprocessingData():
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
    model.fit(x_train, y_train, epochs=1200, batch_size=128)
    df = pd.read_csv('readData.csv')
    dataf = df.values
    dataf = sc.fit_transform(dataf)
    predict = model.predict(dataf)
    predict = model.predict(dataf)
    arr_pred = []
    for i in range(len(predict)):
        arr_pred.append(np.argmax(predict[i]))

    df['prediksi'] = arr_pred

    df.to_csv('HasilPredict.csv', index=False)

    dfHS = pd.read_csv('HasilPredict.csv', index_col=0)
    return dfHS


data_preprocessing = preprocessingData()
print(data_preprocessing)

# print("Status = ", data_preprocessing)

# df['prediksi'] = arr_pred

# df.to_csv('HasilPredict.csv', index=False)
