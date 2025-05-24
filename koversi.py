#latihan konversi pake kalkulator
print("konversi Celcius Ke Suhu Lain")
p = int(input("Masukkan angka : "))
s = (9/5 * p) + 32
print("farenheit :", s, "Farenheit")
z = p*4/5
print("Reamur :", z, "Reamur")
k = p + 273.15
print("Kelvin :", k, "Kelvin")

#pr
#reamur ke kelvin
Reamur = float(input("Masukan Reamur :"))
celcius = Reamur*5/4
kelvin = celcius+273.15
print("R Ke K :", kelvin, "kelvin")
#kelvin ke reamur
kelvin = float(input("Masukkan kelvin :"))
celcius = kelvin-273.15
Reamur = celcius*4/5
print("K ke R adalah :", Reamur, "Reamur")

