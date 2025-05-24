print("="*6 + "Menu Makanan" + "="*6)
print("|1. Nasi Goreng Cumi    |")
print("|2. Nasi Goreng Sapi    |")
print("|3. Nasi Goreng Ayam    |")
print("|4. Nasi Goreng Kambing |")
print("|5. Nasi Goreng Teri    |")
print("|6. Nasi Goreng Jumbo   |")
print("<" + "="*11 + "="*11 + ">")

pesanan = []
while True:
    pilihan = int(input("Masukkan Pesanan Anda (1/2/3/4/5/6) atau 0 untuk selesai: "))
    
    if pilihan == 0:
        break
    elif 1 <= pilihan <= 6:
        pesanan.append(pilihan)
    else:
        print("Pilihan tidak valid. Silakan masukkan angka antara 1 hingga 6.")

if pesanan:
    print("\nPesanan Anda:")
    for item in pesanan:
        if item == 1:
            print("Nasi Goreng Cumi")
        elif item == 2:
            print("Nasi Goreng Sapi")
        elif item == 3:
            print("Nasi Goreng Ayam")
        elif item == 4:
            print("Nasi Goreng Kambing")
        elif item == 5:
            print("Nasi Goreng Teri")
        elif item == 6:
            print("Nasi Goreng Jumbo")
else:
    print("Anda tidak memesan apa pun.")
