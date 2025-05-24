#membuat area gabungan area rentang dari angka
#++++++++=3---------10+++++++++

inputUser = float(input("Masukan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n:"))

#memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang Dari 3 =", isKurangDari)
#memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("lebih dari 10 =4", isLebihDari)

#++++++++=3---------10+++++++++
isCorrect = isKurangDari or isLebihDari
print("angka yang Anda Masudkan :", isCorrect)
#-------3++++++10--------
#kasus irisan
print("\n",10*"=","\n")
inputUser = float(input("Masukan angka yang bernilai\nlebih  dari 3\natau\nkurang dari 10\n:"))
#lebih dari 3
isLebihDari = inputUser > 3
print("Lebih Dari 3 :", isLebihDari)
#kurang dari 10
isKurangDari = inputUser < 10
print("Kurang Dari :", isKurangDari)
#++++++++=3---------10+++++++++
isCorrect = isKurangDari and isLebihDari
print("angka yang Anda Masudkan :", isCorrect)
print("\n",10*"=","\n")
#pr 
#-----0++++++++5-----------8++++++++11-------
inputUser = float(input("Masukkan Angka :"))
a = inputUser > 0
b = inputUser < 5
c = inputUser > 8
d = inputUser < 11

jawaban = a and b or c and d
print("hasilnya: ", jawaban)
#++++++0--------5++++++++8--------11++++++
inputUser = float(input("masukkan angka :"))
a = inputUser < 0
b = inputUser > 5
c = inputUser < 8
d = inputUser > 11

jawaban2 = a and b or c and d
print("hasilnya :", jawaban2)
print