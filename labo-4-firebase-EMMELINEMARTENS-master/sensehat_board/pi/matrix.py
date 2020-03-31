
from sense_hat import SenseHat
import firebase_admin
from firebase_admin import credentials, firestore

# constants
COLLECTION = 'raspcollection'
DOCUMENT = 'sensor-data'

# firebase
cred = credentials.Certificate("../config/keylabo3.json")
firebase_admin.initialize_app(cred)

# sensehat 
sense = SenseHat()
sense.set_imu_config(False, False, False)
sense.clear()

def update_sensehat(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        doc_readable = doc.to_dict()

        rgb_color = doc_readable['matrix']['color']['value']
        status = doc_readable.get('matrix').get('isOn')

        colorRGB = tuple(int(rgb_color[i:i+2],16) for i in (0,2,4))
       
        if status == True :
                sense.set_pixels(colorRGB)
                print('color')
        else:
                sense.clear()
# connect firestore
db = firestore.client()
pi_ref = db.collection(COLLECTION).document(DOCUMENT)
pi_watch = pi_ref.on_snapshot(update_sensehat)

# app
while True:
    pass
