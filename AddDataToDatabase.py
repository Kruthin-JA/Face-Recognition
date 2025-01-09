import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facerecogniton-3c078-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "221181":
        {
            "name": "G.Bharghava",
            "major": "AIML",
            "starting_year": 2022,
            "total_attendance": 1,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "221209":
        {
            "name": "JA.Kruthin",
            "major": "AIML",
            "starting_year": 2022,
            "total_attendance": 1,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

    "221187":
        {
            "name": "G Praneeth",
            "major": "Aiml",
            "starting_year": 2022,
            "total_attendance": 1,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "221223":
        {
            "name": "K .Vamshi ",
            "major": "AIML",
            "starting_year": 2022,
            "total_attendance": 1,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "221236":
        {
            "name": "K.Venkat ",
            "major": "Aiml",
            "starting_year": 2022,
            "total_attendance": 1,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"Julia":
        {
            "name": "Julia ",
            "major": "Aiml",
            "starting_year": 2022,
            "total_attendance": 1,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"Sashirekha":
        {
            "name": "Sashirekha ",
            "major": "Aiml",
            "starting_year": 1994,
            "total_attendance": 1,
            "standing": "b",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}
for key,value in data.items():
    ref.child(key).set(value)