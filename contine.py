# continue pass break 
# pass -> dia berfungsi sebagai dummy dan tidak akan di eksekusi
angka = 0 
while angka < 5:
    angka += 1
    if angka == 3:
        pass

    print(angka)

angka = 0
print(f"Angka Sekarang -->{angka}")
while angka < 5:
        angka += 1
        
        print(f"Angka Sekarang -->{angka}")

        if angka == 3:
            print("Naisee#2")
            continue #angka Membuat Loop Meloncat Ke Step Selanjutnya

        print("Akbarrrrrrrrr") #aksi dua
print("Finish")