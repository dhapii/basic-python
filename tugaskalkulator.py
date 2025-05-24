import math

def menu():
    print("1. Penjumlahan")
    print("2. Perkalian")
    print("3. Pengurangan")
    print("4. Pembagian") 
    print("5. Perpangkatan") 
    print("6. Akar Kuadrat") 
    print("7. Akar Pangkat N") 

def main():
    menu()
    pilihan = float(input('Masukkan Operasi Bilangan (1/2/3/4/5/6/7): '))  # Meminta Input Operasi Dari User

    if pilihan == 6 or pilihan == 7:
        a = float(input('Masukkan Angka: '))  # Hanya angka pertama yang diperlukan untuk akar
        if pilihan == 6:
            hasil = math.sqrt(a)  # Akar kuadrat
            print(f"Akarnya Adalah: {hasil}")
        elif pilihan == 7:
            n = float(input('Masukkan Pangkat Akar (n): '))  # Pangkat untuk akar n
            if n != 0:
                hasil = a ** (1 / n)  # Akar pangkat n
                print(f"Akar Pangkat {n} dari {a} Adalah: {hasil}")
            else:
                print("Error: Pangkat tidak boleh nol.")
    else:
        a = float(input('Masukkan Angka Pertama: '))  # Meminta input angka pertama
        b = float(input('Masukkan Angka Kedua: '))  # Meminta input angka kedua

        if pilihan == 1:  # Penjumlahan
            hasil = a + b
            print(f"Hasil Dari Penjumlahannya Adalah: {hasil}")
            
        elif pilihan == 2:  # Perkalian
            hasil = a * b
            print(f'Hasil Dari Perkaliannya Adalah: {hasil}')
            
        elif pilihan == 3:  # Pengurangan
            hasil = a - b
            print(f'Hasil Dari Pengurangan: {hasil}')
            
        elif pilihan == 4:  # Pembagian
            if b != 0:
                hasil = a / b
                print(f"Hasil Pembagiannya Adalah: {hasil}")
            else:
                print("Error: Tidak Bisa Membagi Dengan 0")
            
        elif pilihan == 5:  # Perpangkatan
            hasil = a ** b
            print(f"Hasil Perpangkatannya Adalah: {hasil}")
            
        else:
            print("Error: Pilihan Tidak Valid")

if __name__ == "__main__":
    main()
