#misal kita punya nilai a dan b
a = 15
b = 12
c = 2007

#penjumlahan
hasil = a + b + c
print(a,'+',b,'+',c,'=',hasil)

hasil = a * b * c
print(a,'*',b,'*',c,'=',hasil)

hasil = a + b - c
print(a,'+',b,'-',c,'=',hasil)

hasil = a / b / c
print(a,'/',b,'/',c,'=',hasil)

#pangkat exponen
hasil = a ** b
print(a,'**',b,'=',hasil)
#modulus 
hasil = a % b
print(a,'%',b,'=',hasil)
#flor division
hasil = a // b
print(a,'//',b,'=',hasil)

#banyak angka
x = 23
y = 22
z = 11
hasil = x + y - z * y ** x / y * x % z
print(x,'+',y,'-',z,'*',y,'**',x,'/',y,'*',x,'%',z,'=',hasil)
#prioritas operasi 
'''
    1. ()
    2. exponen **
    3. perkalian * / ** % //
    4. penjumlahan
'''
a = 11
b = 12
hasil = a + b
print(a, '+', b, '=',hasil)