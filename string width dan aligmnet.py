# width dan multi line

# data
data_nama = "AkbarD'Vennerich"
data_umur = 17
data_tb = 190.8
data_ukuransepatu = 46
data_string = f"nama {data_nama}, umur {data_umur}, tinggi badan {data_tb}, ukuran sepatu {data_ukuransepatu}"
print(5*"="+"Data String"+"="*5)
print(data_string)

#String multiline (dengan menggunakan enter \n)
data_string = f"nama {data_nama} \numur {data_umur} \ntinggi badan {data_tb} \nukuran sepatu {data_ukuransepatu}"
print(5*"="+"Data String"+"="*5)
print(data_string)

# string (kutip triplets)
data_nama = "Akbar"
data_umur = 25  
data_tb = 170   

data_string = f"""
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tb:>5}
"""
print(5*"="+"Data String"+"="*5)
print(data_string)





