# kumpulan data angka
data_angka = [1,2,3,4,5,6,8,6]
print(data_angka)
# kumpulan data string
data_string = ["dhapii","akbar","wibbb"]
print(data_string)
# kumpulan data boolean
data_boolean = [True,False,True,False,False]
print(data_boolean)
# data campuran
data_campuran = [1,"hahaha",False,3]
print(data_campuran)


# cara alternatif bikin list
data_range = range(0,10) #range (start,stop.step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list compehresion
list_pajke_for = [i%2 for i in range(0,10)] #i pertama dapat menjadi operasi perhitungan
print(list_pajke_for)

# membuat list pake for pake if 
list_pake_for_if = [i for i in range(0,10) if i%2 ==0]
print(list_pake_for_if)