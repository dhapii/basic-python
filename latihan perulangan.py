# loopiing
# latihan membuat perulangan segititga
sisi = 20

# menggunakan for (variable dummy)
print("Awal Dari For")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1
print("Akhit Dari For")
# 2. menggunakan while(dummy variable)
print("Awal Dari While")
count = 1
while True:
    print("*"*count)
    count += 1
    if count > sisi:
        break
print("Ahir Dari While")
    

# 3. hanya ganjil saja
print("Awal Dari While")
count = 1
while True:
    print("*"*count)
    count += 1
    if count%2:
        print(f"{count} ganjil")
    
    if count > sisi:
        break
print("Ahir Dari While")

# segitiga sama kaki
print("Awal Dari While")
count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    if count > sisi:
        break
for i in range(5, 0, -1):
    print(" "*(5-i), end='')
    for x in range(i):
        print("+ ", end='')
    print()