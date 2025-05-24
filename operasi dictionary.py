data_dict = {
    "kita":"prikitiw",
    "anda":"piw piw",
    "akbar":"vldg",
    
}

print(data_dict)


# panjang dict
lendict = len(data_dict)
print(lendict)

# mengecek key exist atau tidak

key = "akxb4rr"
checkkey = key in data_dict
print(f"apakaah {key} ada di data dict : {checkkey}")


# mengakses value (read) dengan read 
print(data_dict["kita"])
print(data_dict.get("kita"))
print(data_dict.get("anda"))
print(data_dict.get("kiss","key tidak di temukan"))

# mengudate data 
data_dict["akbar"] = "aku nak acer"
print(data_dict)
data_dict["anda"] = " piw piw piw"
print(data_dict)


data_dict.update({"kita":"axb4rrrrrr"}) 
print(data_dict)
data_dict.update({"nama":"axb4rrrrrr"}) #kalau ga ada di update aja=
print(data_dict)

# menghapus atau delete 
del data_dict["kita"]
print(data_dict)


# looping dictionary 


teman_teman = {
    "cup":"ucup prikitiw",
    "tong":"otong suka nye",
    "dung":"dudung 969",
    "sep":"sepitengh",
    "cuy":"cuyyyyyyyyyy"
}

# looping first yang keluar adalah key 
for teman in teman_teman:
    print(teman)


# operator untuk mengambil item 
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))

values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)

items = teman_teman.items()
print(items)

for item in teman_teman.items():
    print(items)

for key,value in teman_teman.items():
    print(f"key = {key}, value = {value}")



# copy dictionary 

friends = teman_teman.copy()
print(f"ini teman teman {teman_teman}\n")
print(f"ini friends {friends}\n")

teman_teman["cup"] = "ucup prikitiw"
print(f"ini teman teman {teman_teman}\n")
print(f"ini friends {friends}\n")

# pop dictionary (berdasar kan key)

dataAsep = friends.pop("sep")
print(f"Data Asep {dataAsep}")
print(f"friends {friends}")

# popitem dictionary (yang teakhri)

dataTerakhir = friends.popitem()
print(f"Data Terakhir {dataTerakhir}")
print(f"friends {friends}")






























