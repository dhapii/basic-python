import datetime
import os

# Template data mahasiswa
mahasigma_templates = {
    'nama': '',
    'nim': 0,
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 11, 1),
    'lulus': 'Tidak Lulus'
}

data_mahasigma = {}  # Diletakkan di luar loop agar data tidak hilang

while True:
    os.system("cls" if os.name == "nt" else "clear")  # Bersihkan layar

    print(f"{'Selamat Datang':^40}")
    print(f"{'Data Mahasiswa':^40}")
    print("-" * 40)

    # Menggunakan fromkeys untuk membuat dictionary dengan key dari template
    mahasigma = dict.fromkeys(mahasigma_templates.keys())

    # Input data mahasiswa
    mahasigma['nama'] = input("Nama Mahasiswa: ").strip()

    while True:
        try:
            mahasigma['nim'] = int(input("NIM Mahasiswa: "))
            if mahasigma['nim'] in data_mahasigma:
                print("NIM sudah ada, gunakan NIM lain!")
                continue
            if mahasigma['nim'] > 0:
                break
            print("NIM harus berupa angka positif.")
        except ValueError:
            print("Masukkan angka yang valid untuk NIM.")

    while True:
        try:
            mahasigma['sks_lulus'] = int(input("SKS Lulus: "))
            if mahasigma['sks_lulus'] >= 0:
                # Menentukan status lulus/tidak lulus
                mahasigma['lulus'] = "Lulus" if mahasigma['sks_lulus'] > 12 else "Tidak Lulus"
                break
            print("SKS harus angka positif atau nol.")
        except ValueError:
            print("Masukkan angka yang valid untuk SKS.")

    while True:
        try:
            tahun = int(input("Tahun Lahir (YYYY): "))
            bulan = int(input("Bulan Lahir (1-12): "))
            tanggal = int(input("Tanggal Lahir (1-31): "))
            mahasigma['lahir'] = datetime.datetime(tahun, bulan, tanggal)
            break
        except ValueError:
            print("Masukkan tanggal lahir yang valid!")

    # Menyimpan data dengan NIM sebagai key unik
    data_mahasigma[mahasigma['nim']] = mahasigma

    # Menampilkan data mahasiswa yang sudah tersimpan
    print("\nData Mahasiswa Tersimpan:")
    print(f"{'NIM':<10} {'Nama':<20} {'SKS Lulus':<12} {'Tanggal Lahir':<15} {'Status':<12}")
    print("-" * 75)

    for key, mahasiswa in data_mahasigma.items():
        print(f"{key:<10} {mahasiswa['nama']:<20} {mahasiswa['sks_lulus']:<12} {mahasiswa['lahir'].strftime('%d-%m-%Y'):<15} {mahasiswa['lulus']:<12}")

    # Konfirmasi untuk lanjut atau keluar
    is_done = input("\nMau lanjut input data? (y/n): ").strip().lower()
    if is_done == "n":
        break

print("\nAkhir dari program. Terima kasih!")
