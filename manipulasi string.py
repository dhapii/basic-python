#manipulasi string
nama_depan = "Akbar"
nama_tengah = "D"
nama_back = "Villain"
nama_lengkap = nama_depan + " " + nama_tengah + "'" + nama_back
print(nama_lengkap)

#menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

#operator utuk string
#mengecek apakah ada komponen atau string di string

d = "d"
status = d in nama_lengkap 
print(d + " ada di " + nama_lengkap + " = " + str(status))

D = "D"
status = D in nama_lengkap 
print(D + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print(d + "tidak ada di " + nama_lengkap + "=")

#pengulangan string
print("wkwkw"*5)


#indexing
print("index ke-o adalah :" + nama_lengkap[0])
print("index ke-[3:4] adalah :" + nama_lengkap[3:4])
print("index ke-[3:9] adalah :" + nama_lengkap[3:9])
print("index ke-[3,4,5,6,7] adalah :" + nama_lengkap[0:10:2])

#item paling kecil
print("Paling kecil :"  + min(nama_lengkap))

#item paling besar
print("Paling kecil :"  + max(nama_lengkap))

#ascii code
ascii_code = ord(" ")
print("Ascii code untuk spasi adalah :" + str(ascii_code))
data = 17
print("Chart Untuk 11 Adalah", chr(data))
# Assume data is treated as a string, not a raw integer
data = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"

# This is one possible approach assuming each pair of digits represents an ASCII character.
# Adjust the chunk size if necessary based on the expected encoding.
chunk_size = 2  # Example: treating each pair of digits as an ASCII value
result = ''.join(chr(int(data[i:i + chunk_size])) for i in range(0, len(data), chunk_size))
print("Decoded Message: " + result)











