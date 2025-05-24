# pengenalan  fungsi 

def hello_world():
    print("heloo world") #ini adalah operasi/perintah yang akan di eksekusi
    print("Aku adalah Akbar seseorang yang menyesal karena tidak berani")

hello_world() #ini adalah perintah untuk eksekusi dan harus bearda di bawah dari deff 
hello_world()

# not this 
# p()

# def p():
#     print("akbnarrrrr")

# latian

# def nyoba(argument):
#     badan fungsi 
    
def hello_world(nama):
    # fungsi hello world menerima input dengan variable sama 
    print(f"Selemat datang Wahai {nama}")

hello_world("Akbar")

# program tambahan
def tambah(angka_1,angka_2):
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(20,5)
tambah(22,3) #selayaknya fungsi bisa digunakan lebih dari satu

def sayhii(boyband):
    data_nama = boyband.copy()
    for nama in data_nama:
        print(f"YTH {nama}")
angota = ["Dhafi", "akbar", "wibisono"]

sayhii(angota) #apapun yang masuk ke sayhii akan masuk ke boyband








