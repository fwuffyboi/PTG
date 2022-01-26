def takePhoto(photoName):
    import json
    import pygame.camera
    import os
    
    # initializing  the camera
    pygame.camera.init()
    
    # make the list of all available cameras
    camlist = pygame.camera.list_cameras()
    
    # if camera is detected or not
    if camlist:
    
        # initializing the cam variable with default camera
        cam = pygame.camera.Camera(camlist[0], (640, 480))
    
        # opening the camera
        cam.start()
    
        # capturing the single image
        image = cam.get_image()
    
        # saving the image
        with open('../settings.json', 'r') as settingsFile:
            # understand settings data
            data = settingsFile.read()
            obj = json.loads(data)

            mediaFolderLocation = str(obj['media_folder_location'])

        os.chdir(mediaFolderLocation)
        pygame.image.save(image, photoName)
    
    # if camera is not detected the moving to else part
    else:
        print("No camera on current device")
        return "err: no camera"
