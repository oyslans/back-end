import cv2
import face_recognition
import pickle
import os

folderPath = "images"

pathList = os.listdir(folderPath)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    print(fileName)
    # bucket = storage.bucket()
    # blob = bucket.blob(fileName)
    # blob.upload_from_filename(fileName)


def findEncodings(ImagesList):
    encodeList = []
    for img in ImagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


print("\nEncoding Started....\n")
encodeListKnown = findEncodings(imgList)
print("Encoding Completed\n")

encodeListKnownWithIds = [encodeListKnown, studentIds]

file = open("EncodedFile.p", "wb")
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File saved !")
