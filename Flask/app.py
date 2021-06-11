import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import *

app = Flask(__name__)

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

firebaseConfig = {
    "apiKey": "AIzaSyBjj9RHgNh4fw2XImzAkEQT81X1GQ29ZTU",
    "authDomain": "cloudta2021.firebaseapp.com",
    "databaseURL": "https://cloudta2021-default-rtdb.firebaseio.com",
    "projectId": "cloudta2021",
    "storageBucket": "cloudta2021.appspot.com",
    "messagingSenderId": "294938373142",
    "appId": "1:294938373142:web:7d5e9069cfe16bf55f1937",
    "measurementId": "G-P4DT3XSG3W"
}


firebase = pyrebase.initialize_app(firebaseConfig)
dbRealTime = firebase.database()
dbCloud = firestore.client()
relay1 = 0


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form.get('mode'))
        md = request.form.get('mode')
        dbRealTime.child("modes").update({"mode": md})

    return render_template('index.html')


@app.route('/audit', methods=['GET', 'POST'])
def audit():
    doc = dbCloud.collection("Backpropagation").document("relay1")
    doc.set({"pengguna": "fahri", "waktu": 54, "hari": 4, "status": relay1})
    doc = dbCloud.collection("Backpropagation").document("relay2")
    doc.set({"pengguna": "nando", "waktu": 54, "hari": 4, "status": relay1})
    doc = dbCloud.collection("Backpropagation").document("relay3")
    doc.set({"pengguna": "rahel", "waktu": 54, "hari": 4, "status": relay1})
    doc = dbCloud.collection("Backpropagation").document("relay4")
    doc.set({"pengguna": "anya", "waktu": 54, "hari": 4, "status": relay1})

    dbRealTime.child("relay1").update({"relay1": relay1})

    return render_template('audit.html')


if __name__ == '__main__':
    app.run(debug=True)
