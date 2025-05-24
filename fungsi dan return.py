def tambah(a, b):
    hasil = a + b
    return hasil  # Mengembalikan nilai hasil penjumlahan

x = tambah(5, 3)
print(x)  # Output: 8

#dengan return 
def sapa(nama):
    print(f"Halo, {nama}")


sapa("Akbar") #output Halo Akbar
x = sapa("Dhafi")
print(x) #output none karena tidak menggunakan return 

def sapa(nama):
    return f"Halo {nama}!"

x = sapa("Dhafi")
print(x)

#nilai dengan banyak return 
def cek_bilangan(n):
    if n > 0:
        return "Positif"
    elif n < 0:
        return "negatif"
    else:
        return "Nol"
print(cek_bilangan(4))
print(cek_bilangan(-4))
print(cek_bilangan(0))

# fungsi dengan kembalian
def kuadrat(ingka):
    output = ingka**2
    return output


y = kuadrat(3)
x = kuadrat(99)
print(y)
print(x)

print(kuadrat(6))
z = 10 + kuadrat(7)
print(z)

# fungsi return dengan multi input
def tambah(a1,a2):
    return a1 + a2
a = tambah(10,10)
print(a)


def operasimtk(a1,a2):
    tambah = a1 + a2
    kurang = a1 - a2
    kali = a1 * a2
    bagi = a1 / a2

    return tambah,kurang,kali,bagi
k,l,m,n = operasimtk(9,5)


print(f"hasil tambah = {k}")
print(f"hasil Kurang = {l}")
print(f"hasil Kali = {m}")
print(f"hasil bagi = {n}")















