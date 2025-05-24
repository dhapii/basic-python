#tipe data yang g ada komanya (interger)
data_integer = 9999999
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

#tipe data: angka dengan koma (float)
data_float = 1.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))
data_bool = True
print("data : ", data_bool)
print("-bertipe : ", type(data_bool))
data_string = "AkbarTzy"
print("data : ", data_string) 
print("- bertipee : ", type(data_string))
#casting tipe data
#casting adalah merubah tipe data
data_int = 0
data_bool = bool(data_int)  # akan false jika integer 0
print("data_bool:", data_bool)
#INTEGR 
print("<====INTEGER====>")
data_int = 9;
print("data = ", data_int, ",type =",type(data_int))
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data = ", data_float, ",type =", type(data_float))
print("data = ", data_string, ",type =", type(data_string))
print("data = ", data_bool, ",type =", type(data_bool))

#FLOAT
print("<====Float====>")
data_float = 9.5;
print("data = ", data_float, ",type =",type(data_float))
data_int = int(data_float) #akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float)
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_str, ", type =", type(data_str))
print("data = ", data_bool, ",type =", type(data_bool))
#BOOL
print("<====BOOLEAN====>")
data_bool = True;
print("data = ", data_bool, ",type =", type(data_bool))
data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_str, ", type =", type(data_str))
print("data = ", data_float, ",type =", type(data_float))
#String
print("<====String====>")
data_str = "1";
print("data = ", data_str, ",type =", type(data_str))
data_int = int(data_str)    #harus angka
data_float = float(data_str)    #harus angka
data_bool = bool(data_str)  #akan false jika str kosong
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_float, ",type =", type(data_float))
print("data = ", data_bool, ", type =", type(data_bool))

