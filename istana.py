import cv2
import numpy as np

# Membuat canvas gambar dengan ukuran 600x800 dan warna putih
canvas = np.ones((600, 800, 3), dtype="uint8") * 255

# Membuat badan utama istana (persegi panjang)
cv2.rectangle(canvas, (150, 300), (650, 550), (153, 101, 21), -1)

# Membuat pintu tengah istana (persegi panjang)
cv2.rectangle(canvas, (350, 400), (450, 550), (100, 70, 50), -1)

# Membuat menara kiri dan kanan istana (persegi panjang)
cv2.rectangle(canvas, (100, 200), (200, 400), (153, 101, 21), -1)
cv2.rectangle(canvas, (600, 200), (700, 400), (153, 101, 21), -1)

# Membuat atap menara (segitiga) menggunakan poligon
pts_left_tower = np.array([[100, 200], [150, 150], [200, 200]], np.int32)
pts_right_tower = np.array([[600, 200], [650, 150], [700, 200]], np.int32)
cv2.polylines(canvas, [pts_left_tower], isClosed=True, color=(0, 0, 0), thickness=2)
cv2.polylines(canvas, [pts_right_tower], isClosed=True, color=(0, 0, 0), thickness=2)
cv2.fillPoly(canvas, [pts_left_tower], color=(100, 70, 50))
cv2.fillPoly(canvas, [pts_right_tower], color=(100, 70, 50))

# Membuat jendela di menara kiri dan kanan (lingkaran)
cv2.circle(canvas, (150, 250), 20, (255, 255, 255), -1)
cv2.circle(canvas, (650, 250), 20, (255, 255, 255), -1)

# Membuat bendera di menara kiri dan kanan
cv2.line(canvas, (150, 150), (150, 100), (0, 0, 0), 3)
cv2.line(canvas, (650, 150), (650, 100), (0, 0, 0), 3)
cv2.rectangle(canvas, (150, 100), (170, 120), (0, 0, 255), -1)
cv2.rectangle(canvas, (650, 100), (670, 120), (0, 0, 255), -1)

# Menampilkan gambar
cv2.imshow("Istana", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
