#operasi komparasi
#setiap hasil adalah boolean
#>,<,>=,<=,==,!=,is,is not

#>
a = 5
b = 3
print("LEBIH BESAR DARI (>)")
hasil = a > 7
print(a,'>',7,'=',hasil)
hasil = b > 1
print(b,'>',1,'=',hasil)
hasil = a > 5
print(a,'>',5,'=',hasil)
hasil = a > 5.1
print(a,'>',5.1,'=',hasil)

print("LEBIH KECIL DARI (<)")
hasil = a < 7
print(a,'<',7,'=',hasil)
hasil = b < 1
print(b,'<',1,'=',hasil)
hasil = a < 5
print(a,'<',5,'=',hasil)
hasil = a < 5.1
print(a,'<',5.1,'=',hasil)

print("LEBIH BESAR SAMADENGAN (>=)")
hasil = a >= 7
print(a,'>=',7,'=',hasil)
hasil = b >= 1
print(b,'>=',1,'=',hasil)
hasil = a >= 5
print(a,'>=',5,'=',hasil)
hasil = a >= 5.1
print(a,'>=',5.1,'=',hasil)


print("KURANG  DARI SAMA DENGAN (<=)")
hasil = a <= 7
print(a,'<=',7,'=',hasil)
hasil = b <= 1
print(b,'<=',1,'=',hasil)
hasil = a <= 5
print(a,'<=',5,'=',hasil)
hasil = a <= 5.1
print(a,'<=',5.1,'=',hasil)

print("SAMA DENGAN (==)")
hasil = a == 7
print(a,'==',7,'=',hasil)
hasil = b == 3
print(b,'==',3,'=',hasil)

print("SAMA DENGAN (!=)")
hasil = a != 7
print(a,'!=',7,'=',hasil)
hasil = b != 3
print(b,'!=',3,'=',hasil)
#isnotfg
print("object identity(is )")
x = 5 #ini adalah assignment membuat objek
y = 5
print("nilai x =",x,",id = ",hex(id(x)))
print("nilai y =",y,",id = ",hex(id(y)))
hasil = x is y
print("x is y =",hasil)

x = 5 #ini adalah assigment memuat object
y = 6 
print("nilai x = ",x,",id =",hex(id(x)))
print("nilai y = ",y,",id =",hex(id(y)))
hasil = x is y
print("x is y =",hasil)
print("object identity(is not)")
x = 5 #ini adalah assignment membuat objek
y = 5
print("nilai x =",x,",id = ",hex(id(x)))
print("nilai y =",y,",id = ",hex(id(y)))
hasil = x is not y
print("x is not y =",hasil)

x = 5 #ini adalah assigment memuat object
y = 6 
print("nilai x = ",x,",id =",hex(id(x)))
print("nilai y = ",y,",id =",hex(id(y)))
hasil = x is not y
print("x is not y =",hasil)
#operasi logika
#not or xor
#not
print("===NOT===")
a = True
print('Data a =', a)
print('===============NOT')
c = not a
print('Data c =', c)
#OR(akan ture jia salah satu true)
print('===OR===')
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,'=',c)
a = True
b = False
c = a or b
print(a,'OR',b,'=',c)
a = True
b = True
c = a or b
print(a,'OR',b,'=',c)
#AND(akan true jika ke 2nya true)
print('===AND===')
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,'=',c)
a = True
b = False
c = a and b
print(a,'AND',b,'=',c)
a = True
b = True
c = a and b
print(a,'AND',b,'=',c)
#XOR xox^yyyyyy_ (akan true jika salah satu true)
print('===XOR===')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)