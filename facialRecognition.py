def recogniseFace(fileName):
    import json
    from compreface import CompreFace
    from compreface.service import RecognitionService

    DOMAIN: str = 'http://'
    PORT: str = '4086'
    RECOGNITION_API_KEY: str = ''

    with open('settings.json', 'r') as settingsFile:
        # understand settings data
        data = settingsFile.read()
        obj = json.loads(data)
        RECOGNITION_API_KEY = str(obj['RECOGNITION_API_KEY'])

    compre_face: CompreFace = CompreFace(DOMAIN, PORT, {
        "limit": 0,
        "det_prob_threshold": 0.8,
        "prediction_count": 1,
        "status": "true"
    })

    recognition: RecognitionService = compre_face.init_face_recognition(
        RECOGNITION_API_KEY)

    image_path: str = str(fileName)

    print(recognition.recognize(image_path))
    return recognition.recognize(image_path)
