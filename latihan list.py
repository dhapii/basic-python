# program list buku 






list_buku = []
while True:
    print("Masukkan data buku")
    judul = input("Masuukan judul buku\t: ")
    penulis = input("Masuukan penulis buku\t: ")
    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    
    print(f"\nNo.\t| Judul\t\t\t| Penulis")
    print("-"*41)
    for index,buku in enumerate(list_buku):
        print(f"{index + 1}\t| {buku[0]:<16}\t| {buku[1]:<16}")

    
    print("-"*41)
    isLanjut = input("Apakah dilanjutkan?(y/n)")
    if isLanjut == "y":
        continue

    elif isLanjut == "n":
        break

print("Program selesai")










