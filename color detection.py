import cv2
import numpy as np

# Membaca gambar
img = cv2.imread('E:/sekolah/coding/image/nyoba.jpeg')  # Pastikan ini adalah lokasi yang benar


# Mengonversi gambar dari BGR ke HSV
hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Definisi batas bawah dan atas untuk warna yang akan disegmentasi
lower_range = (0, 50, 50)  # Range bawah warna
upper_range = (10, 255, 255)  # Range atas warna

# Membuat mask berdasarkan rentang warna yang ditentukan
mask = cv2.inRange(hsv_image, lower_range, upper_range)

# Menggunakan mask untuk menampilkan warna tertentu
color_image = cv2.bitwise_and(img, img, mask=mask)

# Menampilkan gambar hasil
cv2.imshow('Color Image', color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
