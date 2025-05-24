#episode operator bitwise operator biner,operasi biner,binary
a = 9
b = 5

#bitwise or
c = a + b
print("\n======or======")
print("nilai :",a," , bianary :",format(a,'08b'))
print("nilai :",b," , bianary :",format(b,'08b'))
print('----------------------------(|)')
print("nilai :",c," , bianary :",format(c,'08b'))

#bitwise and (&)
c = a & b 
print("\n=====AND======")
print("nilai :",a," , bianary :",format(a,'08b'))
print("nilai :",b," , bianary :",format(b,'08b'))
print('----------------------------(&)')
print("nilai :",c," , bianary :",format(c,'08b'))

#XOR

c = a ^ b 
print("\n=====AND======")
print("nilai :",a," , bianary :",format(a,'08b'))
print("nilai :",b," , bianary :",format(b,'08b'))
print('----------------------------(^)')
print("nilai :",c," , bianary :",format(c,'08b'))

#bitwise NOT (~)
c = ~a
print("\n=====not======")
print("nilai :",a," , bianary :",format(a,'08b'))
print('----------------------------(~)')
print("nilai :",c," , bianary :",format(c,'08b'))
print('----------------------------(^)')
d = 0b0000001001
e = 0b1111111111
print("nilai :",e^d, " , binary :",format(e^d, "08d"))

#shiftting
#right
c = a << 2
print('\n====<<====')
print("nilai :",a," , bianary :",format(a,'08b'))
print('----------------(<<<<<)')
print("nilai :",c," , bianary :",format(c,'08b'))
#left
c = a >> 2
print('\n====>>====')
print("nilai :",a," , bianary :",format(a,'08b'))
print('----------------(<<<<<)')
print("nilai :",c," , bianary :",format(c,'08b'))