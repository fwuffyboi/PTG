from facialRecognition import recogniseFace
from takePhoto import takePhoto

if __name__ == "__main__":
    tp = takePhoto(photoName="faceToRec.jpg")
    if tp == "err: no camera":
        pass
    else:
        rf = recogniseFace(fileName="faceToRec.jpg")
        print(rf)
