## LIST ##
# Menggunakan kurung siku []
print(3*"=" + " List " + 3*"=")
data_list = [5, 6, 7, 8, 9]
print(data_list)

# Cara mengakses list
print(data_list[0])
print(data_list[1])
print(data_list[2])

# Cara menambahkan data
data_list.append(10)
data_list.append(11)
print(f"Setelah ditambah: {data_list}")

# Cara menghapus data
data_list.remove(10)
data_list.remove(11)
print(f"Setelah dihapus: {data_list}\n")



## TUPLE ##
# Menggunakan kurung lengkung ()

"""
1. elemen tuple tidak dapat diubah
"""
print(3*"=" + " Tuple " + 3*"=")
data_tuple = (1, 2, 3, 4, 5)
print(data_tuple)

# Cara mengakses tuple
print(data_tuple[0])
print(data_tuple[1])
print(data_tuple[2])
print("\n")

## SET ##
# Menggunakan kurung kurawal {}

"""
1. tidak dapat diakses menggunakan indeks
   (krn tidak terurut)
2. elemen set tidak dapat diubah
   (namun bisa ditambah/dihapus)
"""

# Cara menambahkan data 
print(3*"=" + " List " + 3*"=")
data_set = {1, 2, 3, 4, 5}
print(f"Sebelum ditambah: {data_set}")

data_set.add(6)
data_set.add(7)
print(f"Setelah ditambah: {data_set}")

# Cara menghapus data
data_set.remove(6)
data_set.remove(7)
print(f"Setelah dihapus: {data_set}\n")
