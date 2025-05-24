# ototdidak
thislist = ["apple", "gedhang", "mango"]
mylist = thislist.copy()
print(mylist)
mylist = list(thislist)
print(mylist)

mylist = thislist[:]
print(mylist)

# teknik menduplikat list
a = ["akbar", "gaymerabiezzz", "kuda"]
b = a
print(f"a = {a}")
print(f"b = {b}")

a[1] = "dhaftech"
print("Before sort:", b)
b.sort()
print("After sort:", b)

print(f"a = {a}")
print(f"b = {b}")

# memory 
# addres dari kedua list
print(f" addreas a = {hex(id(a))}")
print(f" addreas b = {hex(id(b))}")

print("membuat list c dengan a.copy")
c = a.copy()

print(f" addreas a = {hex(id(a))}")
print(f" addreas b = {hex(id(b))}")
print(f" addreas b = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"b = {c}")

print("kita ubah data 0")
# merubah data hanya merubah di adress yang berbeda bukan di addres yang sama jika addrees sama akan berubah setiap data yang memiliki addres sama 
c[0] = "AkbarTZYy"
print(f"a = {a}")
print(f"b = {b}")
print(f"b = {c}")







