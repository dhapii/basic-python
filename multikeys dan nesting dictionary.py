import datetime as dt
# multikeys dan nesting dictionary 

mahasigma1 = {
    "nama":"akbar prikitiw",
    "panjang":"121212121",
    'lulus':'123',
    'beasigma':False,
    'lahir':dt.datetime(2001,4,5)
}

mahasigma2 = {
    "nama":"akbar str",
    "panjang":"121212121",
    'lulus':'12342',
    'beasigma':True,
    'lahir':dt.datetime(2000,4,5)
}

mahasigma3 = {
    "nama":"akbar kiciwww",
    "panjang":"121212121",
    'lulus':'123',
    'beasigma':False,
    'lahir':dt.datetime(2000,2,4)
}

data_mahasigma = {
    'key1':mahasigma1,
    'key2':mahasigma2,
    'key3':mahasigma3,
}

print(f"{'Key':<6} {'Nama':<17} {'Lulus':<3} {'beasigma':<9} {'lahir':<10}")
print("-"*50)