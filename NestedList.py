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

# Dengan Reference

"""

Jika menggunakan cara ini untuk
menduplikasi nested list, maka 
address yang dimiliki kedua list
akan sama

"""
list_copy = list_peserta.copy()
print("Sebelum Diubah")
print(f"peserta (list copy) = {list_copy}\n")

peserta_0[0] = "michael"
print("Sesudah Diubah")
print(f"peserta (list copy) = {list_copy}")
print(f"peserta (list peserta) = {list_peserta}")
# elemen ke-0 pada dua list tersebut ikut berubah 