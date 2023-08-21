## LIST ##

"""
Pada python, sebuah array
disebut sebagai list.

"""

# list dapat berupa gabungan beberapa tipe data
ini_list = [1, "satu", True, 2, "dua", False] 
print(ini_list)

# cara alternatif membuat list
data_range = range(0, 10, 2) # start, stop, step
data_list = list(data_range) # menggunakan keyword list
print(data_list)

# membuat list dengan for loop
list_dgn_for = [i**2 for i in range(0, 10)] # di pangkat 2
print(list_dgn_for)

# membuat list dengan for loop dan if
list_dgn_for_if = [i for i in range(0, 10) if i != 5] # skip 5
print(list_dgn_for_if)

list_dgn_for_if = [i for i in range(0, 10) if i % 2 == 0] # genap
print(list_dgn_for_if)

list_dgn_for_if = [i for i in range(0, 10) if i % 2 != 0] # ganjil
print(list_dgn_for_if)


## MANIPULASI LIST ##

# dari depan = 0 1 2
# dari belakang = -1 -2 -3
# index = 0(-3)   1(-2)   2(-1)
data = [ "satu",  "dua",  "tiga"]

# mengambil data dari depan
data_pertama = data[0]
print(data_pertama)

# mengambil data dari belakang
data_terakhir = data[-1]
print(data_terakhir)

# mengetahui jumlah data
jumlah_data = len(data) # menggunakan keyword len
print(jumlah_data)

# menambahkan data sesuai posisi (insert)
data.insert(0, "nol") # indeks, item
print(f"data setelah ditambah menggunakan insert : {data}")

# menambahkan data diakhir list (append)
data.append("empat")
print(f"data setelah ditambah menggunakan append : {data}")

# menambahkan dua list
data_baru = ["lima", "enam", "tujuh"]
data.extend(data_baru)
print(f"data setelah digabung menggunakan extend : {data}")

# mengubah data
data[1] = "satuuu"
print(f"data setelah diubah : {data}")

# meremove data
data.remove("satuuu") #harus sesuai besar kecilnya agar tdk error
print(f"data setelah diremove : {data}")

# menghapus data paling belakang
data_akhir = data.pop()
print(f"data akhir = \n{data}")

print(data_akhir)

# ambil posisi data menggunakan index
data_nama = ["Eka", "Hanny", "Oktavia"]

index_nama_pertama = data_nama.index("Eka")
print(f"index eka : {index_nama_pertama}")
index_nama_kedua = data_nama.index("Hanny")
print(f"index hanny : {index_nama_kedua}")

# count data
data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]

jumlah_data_4 = data_angka.count(4)
print(f"jumlah angka 4 : {jumlah_data_4}")
jumlah_data_3 = data_angka.count(3)
print(f"jumlah angka 3 : {jumlah_data_3}")

# mengurutkan list - kecil ke besar
data_angka.sort()
print(f"data angka setelah diurutkan : {data_angka}")

# membalik urutan list - besar ke kecil
data_angka.reverse()
print(f"data angka setelah dibalik urutannya : {data_angka}")












