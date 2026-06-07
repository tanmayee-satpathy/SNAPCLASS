import dlib  # c++/python library for face detection -- > convert face to 128 dimn vector
import numpy as np
import face_recognition_models
from sklearn.svm import SVC # classify face based on embedding patterns
import streamlit as st

from src.database.db import get_all_students

@st.cache_resource # prevents from reloading model repeatedly
def load_dlib_models(): # loads detector,predictor,face embdd model
    detector = dlib.get_frontal_face_detector() 

    sp = dlib.shape_predictor( # detects 68 landmark pts like nose,eye,jaw,lips
        face_recognition_models.pose_predictor_model_location()
    )

    # convert face to embedding vector which gets stored in numpy arr
    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec

def get_face_embeddings(image_np): # takes img as numpy ararys
    detector, sp, facerec = load_dlib_models() # loads cached models
    faces = detector(image_np, 1) # returns all detected faces
  # 1 - upsampling count --> higher val mens detects smaller faces

    encodings= [] # stores embedding 

    for face in faces:
        shape = sp(image_np, face)
        face_descriptor = facerec.compute_face_descriptor(image_np, shape, 1) #128 embedding

        encodings.append(np.array(face_descriptor))
    return encodings

@st.cache_resource
def get_trained_model():
    X = [] # i/p - face embedding
    y = [] # o/p - student id

    student_db = get_all_students()

    if not student_db:
        return None
    
    for student in student_db:
        embedding = student.get('face_embedding')
        if embedding:
            X.append(np.array(embedding))
            y.append(student.get('student_id'))

    if len(X) ==0:
        return None
    
    clf = SVC(kernel='linear', probability=True, class_weight='balanced')

    try:
        clf.fit(X, y)
    except ValueError:
        pass

    return {'clf': clf, 'X':X, "y":y}


def train_classifier(): # retrain model after new student reg
    st.cache_resource.clear()
    model_data = get_trained_model()
    return bool(model_data)

def predict_attendance(class_image_np):
    encodings = get_face_embeddings(class_image_np)

    detected_student = {}

    model_data = get_trained_model()

    if not model_data:
        return detected_student, [], len(encodings)
    
    clf = model_data['clf']
    X_train = model_data['X']
    y_train = model_data['y']

#  get unique student ids
    all_students = sorted(list(set(y_train)))

    for encoding in encodings:
        if len(all_students)>= 2:
            predicted_id= int(clf.predict([encoding])[0])
        else:
            predicted_id = int(all_students[0])

        student_embedding = X_train[y_train.index(predicted_id)]

#   compute euclidean dist
        best_match_score = np.linalg.norm(student_embedding - encoding)

        resemblance_threshold = 0.6

        if best_match_score <= resemblance_threshold:
            detected_student[predicted_id] = True
    return detected_student, all_students, len(encodings)

# flow --->

# classroom img 
#      |
# face detection
#      |
# landmark detection
#      |
# 128D embedding generation 
#      |
# svm classification
#      |
# dist verify
#      |
# attendance marked