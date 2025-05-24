k# format string

# contoh generic

nama = "Akbarrrrrr"
format_str = f"Namaku Adalah {nama}"
print(format_str)

# boolean
boolean = False
format_str = f"Boolean Adalah {boolean}"
print(format_str)

#angka
angkat = 20000.6
format_str = f"Angka Adalah {angkat}"
print(format_str)

# bilangan bulat
bilbul = 15
format_str = f"bilbul adalah {bilbul:d}" #d untuk bilangan tanpa koma
print(format_str)

# ribuan
ribuan = 20000000
format_str = f"Ribuan Adalah {ribuan:,}:" #, memberikan koma pada bilangan ribuan
print(format_str)

# bilangan desinal
angka = 2005.59873309723
format_str = f"desimal = {angka:.2f}" #.2f berarti dua angka di belakang koma
print(format_str)

# menampilkan leading zero
angka = 2005.59873309723
format_str = f"desimal = {angka:010.2f}" #010.2f berarti memberikan 3 0 di depan angka
print(format_str)
#menampilkam tanda +/-
angka_minus = -10
angka_plus = +10.1234567
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)


# memformat persen

persentase = 0.999000
format_persen = f"format persen: {persentase:%}"

print(format_persen)

# melakukan operasi aritmarika di dalam placeholder
harga = 10000
jumlah = 9

format_str = f"Total Belanjaan = {harga*jumlah:,}"
print(format_str)

# Format ke angka lain 
angka = 255
format_binary = f"Binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"Hex = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)






















