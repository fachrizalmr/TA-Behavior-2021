import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import *

app = Flask(__name__)

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(Config)
dbRealTime = firebase.database()
dbCloud = firestore.client()


@app.route('/', methods=['GET', 'POST'])
def index():

    # value untuk mode
    getD = dbRealTime.child('modes').child('mode').get()
    modeP = getD.val()

    # value untuk waktu
    getR1 = dbRealTime.child('relay1').child('waktu').get()
    wkR1 = getR1.val()
    getR2 = dbRealTime.child('relay2').child('waktu').get()
    wkR2 = getR2.val()
    getR3 = dbRealTime.child('relay3').child('waktu').get()
    wkR3 = getR3.val()
    getR4 = dbRealTime.child('relay4').child('waktu').get()
    wkR4 = getR4.val()

    # value untuk status
    getR1 = dbRealTime.child('relay1').child('status').get()
    stR1 = getR1.val()
    getR2 = dbRealTime.child('relay2').child('status').get()
    stR2 = getR2.val()
    getR3 = dbRealTime.child('relay3').child('status').get()
    stR3 = getR3.val()
    getR4 = dbRealTime.child('relay4').child('status').get()
    stR4 = getR4.val()

    # status rubah value dan images
    if stR1 == 1:
        stR1 = "ON"
        img1 = "images/on.png"
    else:
        stR1 = "OFF"
        img1 = "images/off.png"
    if stR2 == 1:
        stR2 = "ON"
        img2 = "images/on.png"
    else:
        stR2 = "OFF"
        img2 = "images/off.png"
    if stR3 == 1:
        stR3 = "ON"
        img3 = "images/on.png"
    else:
        stR3 = "OFF"
        img3 = "images/off.png"
    if stR4 == 1:
        stR4 = "ON"
        img4 = "images/on.png"
    else:
        stR4 = "OFF"
        img4 = "images/off.png"

    if request.method == 'POST':
        print(request.form.get('mode'))
        md = request.form.get('mode')
        dbRealTime.child("modes").update({"mode": md})

    return render_template('index.html', mode=modeP,
                           waktuRelay1=wkR1, waktuRelay2=wkR2, waktuRelay3=wkR3, waktuRelay4=wkR4,
                           statusRelay1=stR1, statusRelay2=stR2, statusRelay3=stR3, statusRelay4=stR4,
                           logoRelay1=img1, logoRelay2=img2, logoRelay3=img3, logoRelay4=img4
                           )


# @app.route('/audit', methods=['GET', 'POST'])
# def audit():
#     doc = dbCloud.collection("Backpropagation").document("relay1")
#     doc.set({
#         "pengguna": "fahri",
#         "waktu": 54,
#         "hari": 4,
#         "status": relay1
#     })
#     return render_template('audit.html')


if __name__ == '__main__':
    app.run(debug=True)
