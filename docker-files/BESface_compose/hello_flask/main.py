import face_recognition
from person_recognition.person_classifier import classify_person
import os
from operator import itemgetter

def is_person(img_fp):
    results = classify_person("person_recognition/tmp/output_graph.pb","person_recognition/tmp/output_labels.txt","Mul","final_result",128,128,img_fp) #todo, 128x128 size may not always be true

    result = max(results, key=itemgetter(1))
    return (result[0] == 'people') and (result[1] >= .60)


def safety_check():

    #check if profiles are of heads
    if not is_person("unknown_left") or not is_person("unknown_right"):
        print "PROFILES ARE NOT PEOPLE, ERR"
        return False

    #check if profiles are not faces
    left_image = face_recognition.load_image_file("unknown_left")
    right_image = face_recognition.load_image_file("unknown_right")

    left_encoding = face_recognition.face_encodings(left_image)
    right_encoding = face_recognition.face_encodings(right_image)
    if len(left_encoding) != 0 or len(right_encoding) != 0:
        print "ERR, FACE FOUND"
        return False
    
    return True
    
def classify(KNOWN_IMAGE_DIR, confidence):

    if not safety_check():
        print "SAFETY CHECK FAILED"
        return None
    
    #load in to-be-classified image
    unknown_image = face_recognition.load_image_file("unknown")  

    # Load the jpg files into numpy arrays
    registered_users = [f for f in os.listdir(KNOWN_IMAGE_DIR) if not f.startswith('.')]

    unknown_encoding = face_recognition.face_encodings(unknown_image)
    if len(unknown_encoding) == 0:
        print "DEBUG: error loading image"
        return None
        
    unknown_face_encoding = unknown_encoding[0]

    result = None
    for user in registered_users:
        #print 'checking user', user
        known_images = []
        curr_dir_pics = [p for p in os.listdir(KNOWN_IMAGE_DIR + user) if not p.startswith('.')]

        for pic in curr_dir_pics:
            known_images.append(face_recognition.load_image_file(KNOWN_IMAGE_DIR + user + "/" + pic))

        # Get the face encodings for each face in each image file
        # Since there could be more than one face in each image, it returns a list of encodings.
        # But since I know each image only has one face, I only care about the first encoding in each image, so grab index 0.
        known_faces = []
        i = 0
        for known_image in known_images:
            encoding = face_recognition.face_encodings(known_image)
            if len(encoding) == 1:
                known_faces.append(encoding[0])
            #else:
            #    print 'IGNORING IMAGE, 0 or >2 FACES FOUND', i, 'len:', len(encoding)
            i += 1
        distances = face_recognition.face_distance(known_faces, unknown_face_encoding)

        #print distances, 'min:', min(distances)

        if min(distances) < confidence:
            #print "FOUND USER:", user
            result = user
            #print "result: ", result
            return result
        #else:
            #print "NOT ACCEPTED:", user

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



