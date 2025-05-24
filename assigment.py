#operasi yang dapat di lakukan penyingkatan 
a = 4 #ini adalah operasi assigment
print("nilai a=", a)

a += 1 #ini adalah penyingkatan dari a = a + 1
print('nilai a+= 1, nilai a menjadi',a)

a -= 1 #ini adalah penyingkatan dari a = a + 1
print('nilai a-= 1, nilai a menjadi',a)

a *= 2 #ini adalah penyingkatan dari a = a + 1
print('nilai a*= 1, nilai a menjadi',a)

a /= 1 #ini adalah penyingkatan dari a = a + 1
print('nilai a/= 1, nilai a menjadi',a)
print("\n")
b = 10 
print("nilai b =", b)
b %= 3
print("milai b%= 3, menjadi",b)
print('\n')
b = 10 
print("nilai b =", b)
b //= 3
print("milai b//= 3, menjadi",b)
b = 6
print("niiai b =", b)
b **= 2
print("nilai b**= 2,menjadi",b)

#xor 
c = True
print("\nnilai c =",c)
c ^= False
print("nilai c ^= false, nilai c menjadi",c)
c = True
print("\nnilai c =",c)
c ^= True
print("nilai c ^= true, nilai c menjadi",c)
#or
c = True
print("\nnilai c =",c)
c |= False
print("nilai c |= false, nilai c menjadi",c)
c = False
print("\nnilai c =",c)
c |= False
print("nilai c |= false, nilai c menjadi",c)
#and
c = True
print("\nnilai c =",c)
c &= False
print("nilai c &= false, nilai c menjadi",c)
c = True
print("\nnilai c =",c)
c &= True
print("nilai c &= true, nilai c menjadi",c)

#geser geser
d = 0b0100
print("\nnilai d =",format(d,'04b'))
d >>= 2
print("nilai d >>= 2, nilai d menjadi",format(d,'04b'))
d <<= 2
print("nilai d <<= 2, nilai d menjadi",format(d,'04b'))