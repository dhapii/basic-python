import cv2
import numpy as np

# Membuat kanvas kosong berwarna putih
image = np.ones((500, 500, 3), dtype='uint8') * 255

# Menggambar bangunan utama (kotak) sebagai rumah
cv2.rectangle(image, (150, 300), (350, 450), (0, 128, 255), -1)  # Warna oranye

# Menggambar atap rumah (segitiga)
pts = np.array([[150, 300], [350, 300], [250, 200]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(image, [pts], isClosed=True, color=(0, 0, 255), thickness=2)  # Warna merah
cv2.fillPoly(image, [pts], (0, 0, 255))  # Mengisi segitiga dengan warna merah

# Menggambar jendela (lingkaran)
cv2.circle(image, (200, 350), 20, (255, 255, 255), -1)  # Jendela kiri, warna putih
cv2.circle(image, (300, 350), 20, (255, 255, 255), -1)  # Jendela kanan, warna putih

# Menggambar pintu (garis)
cv2.rectangle(image, (240, 400), (260, 450), (0, 0, 0), -1)  # Pintu warna hitam

# Menambahkan teks di atas rumah
cv2.putText(image, "Rumah e Axb444RRR", (100, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Menampilkan gambar
cv2.imshow('Tugas Rumah', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
