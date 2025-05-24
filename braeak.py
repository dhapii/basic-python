# data = [1, 2, 3, 4, 5]
# for i in data:
#     print(f"Hallo {i}")

# angka = 0
# while angka < 5:
#     angka += 1
#     print(f"Angka sekarang ---->{angka}")
    
#     if angka == 3:
#         print("Niceee!")
#         break #menghentikan pembacaan program dengan break
    
#     print("wassup")
    
# print("Cukup Finisghhhh")



# data = int(input("Masukkan Angka Sampai= "))

# # Validasi input agar tidak negatif
# if data < 1:
#     print("Angka harus lebih besar dari 0.")
# else:
#     angka = 0
#     while True:
#         angka += 1
#         print(f"Angka sekarang ----> {angka}")
        
#         if angka > 100:
#             print("Mencapai Limitasi")
#             break
#         if angka == data:
#             print("Niceee!")
#             break  # Menghentikan pembacaan program dengan break
#         if data == angka:
#             print("Reached the limit of 100!")
#             break
#         print("wassup")
    
#     print("Cukup Finisghhhh")
import cv2
import numpy as np
img = cv2.imread('image/nyoba.jpeg')   
# Convert the image to grayscale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# Apply a threshold to the image to 
# separate the objects from the background 
ret, thresh = cv2.threshold( 
    gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU) 
  
# Find the contours of the objects in the image 
contours, hierarchy = cv2.findContours( 
    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
  
# Loop through the contours and calculate the area of each object 
for cnt in contours: 
    area = cv2.contourArea(cnt) 
  
    # Draw a bounding box around each 
    # object and display the area on the image 
    x, y, w, h = cv2.boundingRect(cnt) 
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2) 
    cv2.putText(img, str(area), (x, y), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2) 
  
# Show the final image with the bounding boxes 
# and areas of the objects overlaid on top 
cv2.imshow('image', img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 