import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import  storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://facerecogniton-3c078-default-rtdb.firebaseio.com/",
    'storageBucket': "facerecogniton-3c078.appspot.com"
})

folderPath = 'Images'
pathList = os.listdir(folderPath)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = os.path.join(folderPath,path)
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

    #print(os.path.splitext(path)[0])
#the size of the images print(len(imgList))
print(studentIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList




print("Encoding Started......")
enocodeListKnown = findEncodings(imgList)
enocodeListKnownWithIds = [enocodeListKnown, studentIds]
print(enocodeListKnownWithIds)
print("Encoding Complete")


file = open("EncodeFile.p",'wb')
pickle.dump(enocodeListKnownWithIds,file)
file.close()
print("File saved")