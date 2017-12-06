import face_recognition
from credential_manager import set_pass, get_pass
import shutil
import os

KNOWN_IMAGE_DIR = "../known_images"  #todo, make this absolute path

def register_new(url,username,password):
    print "DEBUG: register_new. url=",url,"username=",username,"password=",password
    shutil.move("signupPic.png",KNOWN_IMAGE_DIR + "/known")  #todo, check if image is already there
    set_pass("usernames",url,username)  #todo, what if username="usernames"?
    print "TEST:", get_pass("usernames",url)
    set_pass(url,username,password)

    
def classify(url):
    print "DEBUG: classify"
    #load in to-be-classified image
    unknown_image = face_recognition.load_image_file("loginPic.png")


    # Load the jpg files into numpy arrays
    biden_image = face_recognition.load_image_file("../biden.jpg")
    known_image = face_recognition.load_image_file(KNOWN_IMAGE_DIR + "/known")
    
    # Get the face encodings for each face in each image file
    # Since there could be more than one face in each image, it returns a list of encodings.
    # But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
    known_face_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

    known_faces = [
        biden_face_encoding,
        known_face_encoding
    ]

    # results is an array of True/False telling if the unknown face matched anyone in the known_faces array
    results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

    #print("Biden? {}".format(results[0]))
    #print("Obama? {}".format(results[1]))
    if results[1]:
        if url == "oldHtml":
            url = "newHtml"  #TODO, remove this once demo UI is done
        print "DEBUG: recognized. url=",url
        user = get_pass("usernames",url)
        print "got this user:", user
        password = get_pass(url, user)
        return (user,password)
    else:
        print "DEBUG: not recognized"
        return False


    #print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))



