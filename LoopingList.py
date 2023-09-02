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

