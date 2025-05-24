import cv2
import numpy as np
from keras.models import load_model

# Load model pre-trained untuk ekspresi wajah
model = load_model('model-ekspresi.h5')

# Label yang sesuai dengan kelas pada model
emotion_labels = ['Marah', 'Jijik', 'Takut', 'Bahagia', 'Sedih', 'Kejutan', 'Netral']

# Load Haar Cascade untuk deteksi wajah
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Fungsi untuk mendeteksi ekspresi wajah
def detect_emotion(frame, face_cascade, emotion_model):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray_frame[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

        if np.sum([roi_gray]) != 0:
            roi = roi_gray.astype('float') / 255.0
            roi = np.expand_dims(roi, axis=0)
            roi = np.expand_dims(roi, axis=-1)

            # Prediksi ekspresi wajah
            preds = emotion_model.predict(roi)[0]
            emotion = emotion_labels[preds.argmax()]
            label_position = (x, y)
            
            # Gambar persegi di sekitar wajah dan ekspresi
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, emotion, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    return frame

# Membuka webcam untuk deteksi ekspresi
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Deteksi wajah dan ekspresi
    frame = detect_emotion(frame, face_cascade, model)

    # Tampilkan frame dengan ekspresi terdeteksi
    cv2.imshow('Ekspresi Wajah', frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
