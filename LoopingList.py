list = [0, 1, 2, 3, 4, 5]

# For Loop
print("\nFor Loop")
i = 0 # variabel utk menampilkan index

for angka in list:
    i += 1
    print(f"angka ke-{i} adalah: {angka}")

# While Loop
print("\nWhile Loop")
panjang = len(list)
index = 1 # variabel utk menampilkan index
i = 0

while i < panjang:
    print(f"angka ke-{index} adalah: {list[i]}")
    index += 1
    i += 1

# List Comprehension
print("\nList Comprehension")
data = ["Eka", 9,  "Hanny", 10, "Oktavia", 11]
[print(f"data : {i}") for i in data]

# Enumerate
print("\nEnumerate")
data = ["Eka", 9,  "Hanny", 10, "Oktavia", 11]

for index, data in enumerate(data):
        print(f"elemen ke-{index} adalah: {data}")

## LATIHAN -> PROGRAM LIST BUKU ##

list_buku = []

while True:
    print("\nMasukkan Data Buku")
    judul = input("Judul Buku: ")
    penulis = input("Penulis Buku: ")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)

    print("\n\n","="*10,"Data Buku","="*10)
    
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")
    
    print("\n\n","="*20)

    isLanjut = input("Apakah Dilanjutkan? (y/n) \n =>")

    if isLanjut == "n":
        break
print("PROGRAM SELESAI")



