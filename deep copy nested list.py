data_0 = [1,2]
data_1 = [3,4]
data_2d = [data_0,data_1,10]#like this
data_2d_copy = data_2d.copy()
print(f"data = {data_2d}")
print(f"data copy = {data_2d_copy}")
# cara mengambil data dari nested list 
data = data_2d[1][1]
print(f"data = {data}")

# addres semua
print(f"addres asli dari dara 2d {hex(id(data_2d))}")
print(f"addres copy dari dara 2d {hex(id(data_2d_copy))}")

print("addres dari member 1")
# addres semua
print(f"addres asli dari dara 2d {hex(id(data_2d[0]))}")
print(f"addres copy dari dara 2d {hex(id(data_2d_copy[0]))}")
data_2d[1][0] = 5
data_2d[2] = 9
print(f"data = {data_2d}")
print(f"data copy = {data_2d_copy}") 


# saat mengcopy yang di copy adalah yang bukan list alias addresnya dan jika ingin mencopy maka haru s menggunakan deep list copy 

# deep copy 
from copy import deepcopy
data_2d = [data_0,data_1,10]
data_2d_deepcopy = deepcopy(data_2d)

print(f"addres asli = {hex(id(data_2d))}")
print(f"addres deep = {hex(id(data_2d_deepcopy))}")

print(f"addres asli dari dara 2d {hex(id(data_2d[0]))}")
print(f"addres copy dari dara 2d {hex(id(data_2d_deepcopy[0]))}")

data_2d[1][0] = 30
data_2d[2] = 2
print(f"data = {data_2d}")
print(f"data copy = {data_2d_copy}")
print(f"data copy = {data_2d_deepcopy}")



# jadi kesimpulan nya adalah kalau kita punya member like nested list maka kita tidak bisa menngunakan copy biasa harus menggunakan deep copy





