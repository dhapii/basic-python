import cv2
import numpy as np
import math
import datetime

# Fungsi untuk menggambar jarum jam
def draw_hand(img, angle, length, color, thickness):
    # Mengambil ukuran tengah lingkaran
    center = (img.shape[1] // 2, img.shape[0] // 2)
    
    # Menghitung titik akhir jarum jam
    y = int(center[1] - length * math.sin(angle))
    x = int(center[0] + length * math.cos(angle))
    
    # Menggambar jarum jam
    cv2.line(img, center, (x, y), color, thickness)

# Fungsi untuk menggambar jam analog
def draw_clock(img, time):
    # Radius jam dan titik pusat
    radius = min(img.shape[1], img.shape[0]) // 2 - 20
    center = (img.shape[1] // 2, img.shape[0] // 2)
    
    # Menggambar lingkaran luar
    cv2.circle(img, center, radius, (255, 255, 255), 2)

    # Mengambil waktu saat ini
    hours, minutes, seconds = time.hour % 12, time.minute, time.second

    # Menghitung sudut untuk setiap jarum jam (dalam radian)
    second_angle = math.radians(6 * seconds)  # 360° / 60 detik = 6° per detik
    minute_angle = math.radians(6 * minutes + seconds / 10.0)  # 360° / 60 menit = 6° per menit
    hour_angle = math.radians(30 * hours + minutes / 2.0)  # 360° / 12 jam = 30° per jam

    # Menggambar jarum detik (panjang penuh)
    draw_hand(img, second_angle, radius - 20, (0, 0, 255), 2)

    # Menggambar jarum menit (lebih pendek)
    draw_hand(img, minute_angle, radius - 40, (255, 255, 255), 4)

    # Menggambar jarum jam (lebih pendek)
    draw_hand(img, hour_angle, radius - 60, (255, 255, 255), 6)

# Main loop
if __name__ == "__main__":
    # Ukuran gambar jam
    img_size = 400

    # Membuat window untuk jam analog
    cv2.namedWindow("Analog Clock", cv2.WINDOW_NORMAL)

    while True:
        # Membuat kanvas kosong (hitam)
        img = np.zeros((img_size, img_size, 3), dtype=np.uint8)
        
        # Mendapatkan waktu saat ini
        current_time = datetime.datetime.now()

        # Menggambar jam
        draw_clock(img, current_time)

        # Menampilkan gambar jam
        cv2.imshow("Analog Clock", img)

        # Menunggu 1 detik sebelum mengupdate
        if cv2.waitKey(1000) & 0xFF == ord('q'):
            break

    # Menutup semua window
    cv2.destroyAllWindows()
