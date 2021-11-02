import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

config = {
  'apiKey': "AIzaSyBrEqI6eebrQdYb7nz1xH5onyPmuYb0CWc",
  'authDomain': "biometric-adb.firebaseapp.com",
  'projectId': "biometric-adb",
  'storageBucket': "biometric-adb.appspot.com",
  'messagingSenderId': "273893549802",
  'appId': "1:273893549802:web:f05b5fc453ee52bb375993",
  'measurementId': "G-ZT7GST6XVX"
}

cred = credentials.Certificate('firebase-adminsdk.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection('teste').document('teste2')

doc_ref.set({
  'nome' : 'antonio',
  'cidade' : 'sao paulo'
})

