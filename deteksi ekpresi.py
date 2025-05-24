import cv2
from sklearn.svm import SVC
import numpy as np

# Load face detection model (e.g., Haar cascade)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load expression classification model (e.g., SVM)
svm = SVC(kernel='linear', C=1)

# Define feature extraction function (e.g., facial landmarks)
def extract_features(face):
    # Extract facial landmarks (e.g., eyes, nose, mouth)
    landmarks = ...
    # Compute feature vector from landmarks
    features = ...
    return features

# Load dataset of labeled facial expressions
expressions = ...

# Train expression classification model
svm.fit(expressions[:, :-1], expressions[:, -1])

# Load video stream or image
cap = cv2.VideoCapture(0)  # or load an image file

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect faces in frame
    faces = face_cascade.detectMultiScale(frame)

    for face in faces:
        # Extract features from detected face
        features = extract_features(face)
        # Classify expression using trained model
        predicted_expression = svm.predict(features)
        # Draw bounding box and expression label on frame
        cv2.rectangle(frame, (face[0], face[1]), (face[0] + face[2], face[1] + face[3]), (0, 255, 0), 2)
        cv2.putText(frame, predicted_expression, (face[0], face[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow('Expression Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()