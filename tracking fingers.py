import cv2
import mediapipe as mp
import numpy as np

# Inisialisasi Mediapipe dan OpenCV
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

# Membuat gambar hitam untuk menggambar jejak
canvas = None

# Inisialisasi video capture
cap = cv2.VideoCapture(0)

# Variabel untuk menyimpan posisi sebelumnya
prev_x, prev_y = None, None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Membalikkan gambar agar sesuai dengan pandangan seperti cermin
    frame = cv2.flip(frame, 1)

    # Konversi gambar ke RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    # Inisialisasi canvas untuk jejak jika belum ada
    if canvas is None:
        canvas = np.zeros_like(frame)

    # Jika tangan terdeteksi
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Ambil landmark titik ujung jari telunjuk (id = 8)
            index_finger_tip = hand_landmarks.landmark[8]
            h, w, _ = frame.shape
            x, y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)

            # Jika ada posisi sebelumnya, gambar garis dari posisi sebelumnya ke posisi sekarang
            if prev_x is not None and prev_y is not None:
                cv2.line(canvas, (prev_x, prev_y), (x, y), (0, 255, 0), 5)

            # Update posisi sebelumnya dengan posisi saat ini
            prev_x, prev_y = x, y

            # Gambar landmark tangan di frame asli
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Gabungkan frame dan canvas
    frame = cv2.add(frame, canvas)

    # Tampilkan frame
    cv2.imshow('Hand Tracking with Line', frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Membersihkan
cap.release()
cv2.destroyAllWindows()
