## DICTIONARY (DICT) ##
# Associative array -> pasangan key value

data_dict = {
    # 'key' : 'value',
    'sisfo' : 'Sistem Informasi',
    'aktu' : 'Ilmu Aktuaria',
    'math' : 'Matematika'
}

print(data_dict['sisfo'])


##############################################


## OPERATOR DICTIONARY ##

# Panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# Mengecek key exist atau tidak
KEY = "aktu"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}") 

# Mengakses value (read) dengan get
print(data_dict["sisfo"]) # cara 1
print(data_dict.get("sisfo")) # cara 2
# cek key dengan message tidak ditemukan
print(data_dict.get("chem","Key Tidak Ditemukan")) 

# Mengupdate data
data_dict["sisfo"] = "Sistem Informasi 2021" # mengganti value yg sdh ada
print(data_dict)

data_dict.update({"sisfo":"Sistem Informasi"}) # mengganti value yg sdh ada
print(data_dict)

data_dict.update({"chem":"Kimia"}) # jika value blm ada, akan ditambahkan yg baru
print(data_dict)

# mendelete data pada dictionary
del data_dict["chem"]
print(data_dict)


##############################################


## LOOPING DICTIONARY ##

# Untuk mengambil key
keys = data_dict.keys()
print(keys)

for key in data_dict.keys():
	print(key)

# Untuk mengambil value
values = data_dict.values()
print(values)

for value in data_dict.values():
	print(value)

# Untuk mengambil key & value
items = data_dict.items()
print(items)

for item in data_dict.items():
	print(item)

for key,value in data_dict.items():
	print(f"key = {key}, value = {value}")


##############################################

## COPY DICTIONARY ##

"""

Untuk menduplikat dict, gunakan
.copy() agar hasil duplikatnya
menjadi satu kesatuan yang berbeda

"""

data_dict_copy = data_dict.copy()
print(f"data dict asli : {data_dict}\n")
print(f"data dict copy : {data_dict_copy}\n")

## POP & POPITEM DICT ##

# Pop : mengeluarkan sebuah elemen dari dict
data_sisfo = data_dict.pop("sisfo")
print(f"data sisfo : {data_sisfo}\n")
print(f"data dict (setelah di pop) : {data_dict}\n")

# Pop Item : mengeluarkan elemen terakhir dari dict
data_terakhir = data_dict.popitem()
print(f"data terakhir : {data_terakhir}\n")
print(f"data setelah di pop item : {data_dict}\n")
