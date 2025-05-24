# otodidak
list1 = ["fisika", "kimia" , "sija", 2007]
list2 = [1, 2, 3, 4, 5, 6,]
list3 = ["a", "k", "b", 4, "r"]
print(list3)
print ("list[0]: ", list2[0])
print ("list[0]: ", list1[3])

list2[1] = 1945
print(f"List pembaruan dari index2: ", list2[1])

print(list3)
del list3[2]
print("setelah di hapus nilai pada index 2 : ", list3)



print(f"panjang list 1 adalah : {len(list1)}" )

print(f"Panjang list 1 adalah : {max(list2)}")

print(f"Panjang list 1 adalah : {min(list2)}")

# youtube
data_angka  = [1,1,15,5,7,9,0,87,1,1,2,2,2,2,2,2,3,4,5,6,7,8,9,0]
print(f"data angka adalah = \n{data_angka}")
# count data

jumlah_data_1 = data_angka.count(1)
jumlah_data_2 = data_angka.count(1)
print(f"jumlah angka 1 adalah {jumlah_data_1} dan angka 2 berjumlah {jumlah_data_2}")
# ambil possisi data 
data = ["Akbar", "ujang", "duyung", "axb4rr"]
print(f"data = {data}")

data_axb4rrr = data.index("axb4rr")
print(f"data axbar adalah {data_axb4rrr}")

# mengurutkan list 
print(f"data angka sebelum sort {data_angka}")
data_angka.sort()
print(f"data setelah di sort {data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort {data}")

# balik listnya 
print(f"data = {data} \n {data_angka}")
data.reverse()
data_angka.reverse()
print(f"data reversed \n {data} \n {data_angka}")
 
# #  penasaran 
# data_random = ["akbar", 2,3,4,3,2,2,67,4,3465, "akbar.tech"]
# print(f"data = {data_random}")
# data_random.sort()
# print(f"data random sort {data_random}")
# eror string dab interger tudak bisa di sort tanpa filter tetapi masih bisa di maksukkan kedalam lisr 
# simple nya sort untuk single type

# penyelesaian dengan di filter terlebih dahulu 


data_random = ["akbar", 2,3,4,3,2,2,67,4,3465, "setup gaming"]
print(f"data = {data_random}")


stringzz = [item for item in data_random if isinstance(item, str)]
numberzz = [item for item in data_random if isinstance(item, int)]

# sort eaach list
stringzz.sort()
numberzz.sort()

# paling bisa di gabung seoerti ini 
print(f"gabunagn {stringzz} dan {numberzz}")















