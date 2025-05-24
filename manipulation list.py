# operasi

# index 0(-3) 1(-2) 2(-1)

data = ["Akbar","otong","El"]

# mengambil data dari list ini 
data_o = data[0]
print(f"data pertama (index 0) = {data_o}")

data_terakhir = data[-1]
print(f"data teakhir adalah = {data_terakhir}")


data_ucup = data[-3]
print(f"data ucup = {data_ucup}")


# mengambil info jumlah 
panjang_data = len(data)
print(f"penjang data = {panjang_data}")

# manipulasi data list
# menambahkan item pada data list 
print(f"data sebelum di tambah \n{data}")

# di awal
data.insert(1,"Akbar")
print(f"data setelah di tambah = \n{data}")

# di tengah
data.insert(2,"rrq akbar")
print(f"data setelah di tambah = \n{data}")


# menambah di akhir 
data.append("Evos akbar")
print(f"data du tambaj lagi = \n{data}")
# menambahkan list dengan list
data_baru = ["uang","epos","axbar"]
data.extend(data_baru)
print(f"data gabungan =\n{data}")

# merubah data
data[2] = "maykel"
print(f"data rubah = \n{data}")

# meremove jika data yang di remove tidak ada di list maka akan eror
data.remove("epos")
print(f"data remove \n{data}")

# meremove data paling belakang
data_akhir = data.pop()
print(f"data Akhir = \n{data}")
print(data_akhir)