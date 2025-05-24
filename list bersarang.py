# list bersarang 
data_0 = [1,2]
data_1 = [3,4]
data_list_biasa = [1,2,3,4,5,6]
print(f"list biasa = {data_list_biasa}")
list_2d = [data_0,data_1,data_list_biasa]
print(f"list 2D = {list_2d}")

# contoh penggunaan


player_0 = ["akbarTZY",17,"man"]
player_1 = ["lista",17,"female"]
player_2 = ["esokkolahtakcikgu",17,"non ordinarry"]
list_peserta = [player_0,player_1,player_2]
print(f"peserta = {list_peserta}")

for player in list_peserta:
    print(f"nama\t: {player[0]}")
    print(f"umur\t: {player[1]}")
    print(f"gender\t: {player[2]}\n")

# permasalahan dengan refrence n

list_copy = list_peserta.copy()
print(f"peserta= {list_copy}")
player_0[0] = "maykel"
print(f"peserta= {list_copy}")
print(f"peserta = {list_peserta}")