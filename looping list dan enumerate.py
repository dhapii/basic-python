# looping dari list 

# for loop
print("\nFor loop") 
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
    print(f"Angka = {angka}")

peserta = ["akbar","akbarss","akbuar"]

for nama in peserta:
    print(f"Nama = {nama}")


# for loop dan range 
print("\nFor loop dan range") 
kumpulan_angka = [10,5,6,4,3,3,2,4]
panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")


# while 
print("\nwhile") 

kumpulan_angka = [10,5,6,4,3,3,2,4]
panjang = len(kumpulan_angka)
i = 0 

while i < panjang:
    print(f"angka = {kumpulan_angka}")

    i += 1

# list compperahension 

data = ["akbar",1,2,4,55,"axb4rr"]

[print(f"data = {i}") for i in data]

angka = [10,5,6,4,3,3,2,4]

aka_kuadrat = [i**2 for i in angka]
print(f" Angka kuadrat = {aka_kuadrat}")
# enumerate 
print("\n enumerate")
data_list = ["akbar",1,2,4,55,"axb4rr"]
for index,data in enumerate(data_list):
    print(f"Index = {index}, data = {data}")











