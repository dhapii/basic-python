import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar dari file
img = cv2.imread('image/a.jpg', cv2.IMREAD_GRAYSCALE)

# Menggunakan Canny edge detection
edges = cv2.Canny(img, 100, 200)

# Menampilkan hasil
plt.figure(figsize=(11, 7))

# Gambar asli
plt.subplot(121)  # Perbaiki dari sublot ke subplot
plt.imshow(img, cmap="gray")
plt.title('Gambar Asli')
plt.xticks([])  # Menghilangkan tick pada sumbu x
plt.yticks([])  # Menghilangkan tick pada sumbu y

# Hasil deteksi tepi
plt.subplot(122)  # Perbaiki dari sublot ke subplot
plt.imshow(edges, cmap="gray")
plt.title('Deteksi Tepi dengan Canny')
plt.xticks([])  # Menghilangkan tick pada sumbu x
plt.yticks([])  # Menghilangkan tick pada sumbu y

plt.show()
