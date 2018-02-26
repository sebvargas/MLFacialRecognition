import face_recognition
import os


def classify(KNOWN_IMAGE_DIR):

    #load in to-be-classified image
    unknown_image = face_recognition.load_image_file("unknown")
    

    # Load the jpg files into numpy arrays
    registered_users = [f for f in os.listdir(KNOWN_IMAGE_DIR) if not f.startswith('.')]
    #registered_users = os.listdir(KNOWN_IMAGE_DIR)

    unknown_encoding = face_recognition.face_encodings(unknown_image)
    if len(unknown_encoding) == 0:
        print "DEBUG: error loading image"
        return None
        
    unknown_face_encoding = unknown_encoding[0]
    

    for user in registered_users:
        known_images = []
        curr_dir_pics = [p for p in os.listdir(KNOWN_IMAGE_DIR + user) if not p.startswith('.')]
        for pic in curr_dir_pics:
            known_images.append(face_recognition.load_image_file(KNOWN_IMAGE_DIR + user + "/" + pic))

        # Get the face encodings for each face in each image file
        # Since there could be more than one face in each image, it returns a list of encodings.
        # But since I know each image only has one face, I only care about the first encoding in each image, so grab index 0.
        known_faces = []
        for known_image in known_images:
            known_faces.append(face_recognition.face_encodings(known_image)[0])



        distances = face_recognition.face_distance(known_faces, unknown_face_encoding)

        print distances, 'min:', min(distances)

        if min(distances) < .5:
            print "FOUND USER:", user
            result = user
        else:
            print "NOT ACCEPTED:", user

    return result
'''    
        # results is an array of True/False telling if the unknown face matched anyone in the known_faces array
        results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

        result = None
        for i in range(len(registered_users)):
            if results[i]:
                result = registered_users[i]
                break
        return result
'''



