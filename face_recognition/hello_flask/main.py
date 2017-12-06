import face_recognition
import shutil
import os

KNOWN_IMAGE_DIR = "known_images/"  #todo, make this absolute path

def register_new(username):
    print "DEBUG: register_new. username=",username
    shutil.move("signupPic.png",KNOWN_IMAGE_DIR + username)  #todo, check if image is already there

    
def classify():
    print "DEBUG: classify"
    #load in to-be-classified image
    unknown_image = face_recognition.load_image_file("unknown")
    

    # Load the jpg files into numpy arrays
    registered_users = [f for f in os.listdir(KNOWN_IMAGE_DIR) if not f.startswith('.')]
    #registered_users = os.listdir(KNOWN_IMAGE_DIR)

    known_images = []
    for user in registered_users:
        known_images.append(face_recognition.load_image_file(KNOWN_IMAGE_DIR + user))

    # Get the face encodings for each face in each image file
    # Since there could be more than one face in each image, it returns a list of encodings.
    # But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
    known_faces = []
    for known_image in known_images:
        known_faces.append(face_recognition.face_encodings(known_image)[0])

    check_size = face_recognition.face_encodings(unknown_image)
    if len(check_size) == 0:
        print "DEBUG: error loading image"
        return None
        
    unknown_face_encoding = check_size[0]

    # results is an array of True/False telling if the unknown face matched anyone in the known_faces array
    results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

    result = None
    for i in range(len(registered_users)):
        if results[i]:
            result = registered_users[i]
            break
    return result




