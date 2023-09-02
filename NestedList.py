## NESTED LIST ## 
data_list_biasa = [0, 1, 2, 3, 4, 5]
print(f"data list biasa : {data_list_biasa}")

data_0 = [6, 7]
data_1 = [1, 2, 3]
nested_list = [data_0, data_1, 9, 5]
print(f"nested list : {nested_list}")

# Contoh Penggunaan
peserta_0 = ["Eka",20,"Wanita"]
peserta_1 = ["Dwi",15,"Pria"]
peserta_2 = ["Tri",50,"Wanita"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"peserta = {list_peserta}")

for peserta in list_peserta:
	print(f"nama\t: {peserta[0]}")
	print(f"umur\t: {peserta[1]}")
	print(f"gender\t: {peserta[2]}\n")

# Dengan Copy

list_copy = list_peserta.copy()
print("Sebelum Diubah")
print(f"peserta (list copy) = {list_copy}\n")
print(f"address list peserta asli : {hex(id(list_peserta))}")
print(f"address list peserta copy : {hex(id(list_copy))}")


peserta_0[0] = "Hanny"
print("Sesudah Diubah")
print(f"peserta (list copy) = {list_copy}")
print(f"peserta (list peserta) = {list_peserta}\n")
"""
elemen ke-0 pada dua list tersebut ikut berubah 
-> harus menggunakan deepcopy
"""

# Mengambil Data dari Nested List
data = nested_list[0][1]
print(f"Data kedua pada list pertama dalam nested list : {data}\n")

nested_list_copy = nested_list.copy()
print(f"nested list : {nested_list}")
print(f"nested list (copy) : {nested_list_copy}")

# memiliki address yang berbeda
print(f"address asli = {hex(id(nested_list))}") # address beda
print(f"address copy = {hex(id(nested_list_copy))}") # address beda


""""

Walaupun kedua nested list tsb memiliki
address yang berbeda, namun elemen didalamnya
masih memiliki address yang sama sehingga untuk
menduplikat elemen dalam nested list harus
menggunakan deepcopy

"""
print("address dari member ke-1")
print(f"address asli = {hex(id(nested_list[0]))}") # address sama
print(f"address copy = {hex(id(nested_list_copy[0]))}\n") # address sama

## DEEPCOPY ##

from copy import deepcopy

nested_list = [data_0,data_1,10]
nested_list_deepcopy = deepcopy(nested_list)

print(f"address asli = {hex(id(nested_list))}")
print(f"address deep = {hex(id(nested_list_deepcopy))}\n")

print("address dari member ke-1")
print(f"address asli = {hex(id(nested_list[0]))}")
print(f"address copy = {hex(id(nested_list_deepcopy[0]))}\n")

nested_list[1][0] = 30
print(f"data = {nested_list}")
print(f"data deep = {nested_list_deepcopy}\n")


