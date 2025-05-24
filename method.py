#operator dalam bentuk method

#membuat case dari string

salam = "Syalom"
print("Normal =", salam)

salam = salam.upper()
print("upper =", salam)

salam = salam.lower()
print("lower =", salam)
salam = "SIST"
apakah_lower = salam.islower()
print(salam + " is lower =" + str(apakah_lower)) 
apakah_upper = salam.isupper()
print(salam + " Is upper =" + str(apakah_upper))

#isalpha() <---- untuk mengecek semua huruf 
#isalnum() <---- huruf dan angka
#isdecimal()  <--- angkaaaaaa saja
#issspace()  <-----spasi,tab,new line \n
#istitle() <--- Semua Kata di mulai dari huruf besar

judul = "akbar si orang baik hatii dan kutu buku"
x = judul.title()
print("Title :" + x)
sample = "Akbarawrrrw123"
apakah_num = sample.isalnum()
print(sample + "Isalnum :", str(apakah_num))
x = "Akbar Si Orang Baik Hatii Dan Kutu Buku"
apakah_title = x.istitle()
print(x + "\nApakah is title :", str(apakah_title))

x = "Akbar's Si Orang Baik Hatii Dan Kutu Buku"
apakah_title = x.istitle()
print(x + "\nApakah is title :", str(apakah_title))
# mengecek komponen startswith() endswith() <---- keren
cek_start = "Akbar Si Global Gord".startswith("Akbar")
print("start :" + str(cek_start))
cek_end = "Akbar SI Global gord".endswith("gord")
print("end :" + str(cek_end))
# komponen join() dan split()

pisah = ['akbar','voldi','goadddd']
print(pisah)
gabungan = ' '.join(pisah) #fungsi '' pemberi jeda di samping kata
print(gabungan)
gabungan = "Akbaryvoldiygoadddd"
print(gabungan.split('y'))

# alokasi karakter dengan ljust() dan rjust()
# kanan
kanan = "kanan".rjust(10)
print("<"+kanan+">")
# kiri
kiri = "kiri".ljust(10)
print("<"+kiri+">")
# tengah
tengah = "tengah".center(10,".")
print("<"+tengah+">")
# kebalikanya  -----> strip 
tengah = "tengah".strip()
print("<"+tengah+">")