# Membuat sebuah string
data = "ini adalah string"

# Mencetak string
print(data)

# Menampilkan tipe data dari variabel 'data'
print(type(data))

print('menggunakan single quote')
print("menggunakan qouble quote")
'''
    1.menggunakan double quote '....'
    2.menggunakan double quote "...."
'''
data = 'ini adalah hari jum\'at'
print(data)

data = "g\'day, isn\'t"
print(data)

data = "C\\user\\Akbar"
print(data)
data = "Akbar\t\t\t\tLss"
print(data)
data = "Akbar\bS"
print(data)
#newline
#\nl\n LF line feed haynya untuk linux
#\n CR carriage return hanya untuk macos

print("Akbar\r\n Always\r\n K")

#string literal & raw
#salah
print("C:\new folder")
#true
print(r"C:\new folder")

#multiline
print("""
Nama : Akbar
Kelas : XII Sija 2
Mole : Akbar Voldigoad.
""")