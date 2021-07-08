
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

data = {'pengguna': 'Rudi', 'status': 'ON', 'idrelay': 1,
        'akurasi': 0.98, 'loss': 0.12, 'interval': 2}

db.collection('Kamis 8 July 2021').document(
    'anya').collection('8.07').document('relay1').set(data)
db.collection('Kamis 8 July 2021').document(
    'fachri').collection('8.07').document('relay1').set(data)
