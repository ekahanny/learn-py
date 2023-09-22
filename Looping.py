## LOOPING ##

# For Loop #

"""
for kondisi:
    aksi
"""

# For loop menggunakan list
angka_list = [0, 1, 2, 3, 4]

for i in angka_list:
    print(f"i sekarang bernilai => {i}")
print("Akhir program loop dengan list \n")

# For loop menggunakan range
angka_range = range(5)

for index in angka_range:
    print(f"index sekarang bernilai => {index}")
print("Akhir program loop dengan range 1 \n")

for i in range(1, 5): #dimulai dari 1, berakhir sebelum 5
        print(f"i sekarang bernilai => {i}")
print("Akhir program loop dengan range 2 \n")

# For Loop menggunakan string
data_str = "pemrograman"

for huruf in data_str:
    print(huruf)
print("Akhir dari loop dengan string \n")

# While Loop #

"""
1. While loop akan mengevaluasi kondisi yang dimasukkan
2. Jika kondisi bernilai true, maka while loop akan dieksekusi
3. Kondisi akan dievaluasi kembali
4. Perulangan akan terus berjalan hingga kondisi bernilai false
5. Ketika kondisi bernilai false, maka loop akan berhenti

"""

# looping dari 1-5
print(5*"=" + "While Loop" + 5*"=")
i = 0

while i < 5:
    i += 1
    print(i)

# menjumlahkan angka

angka = int(input("Masukkan jumlah angka yang ingin ditambah : "))

i = 1
jumlah = 0

while i <= angka:
    jumlah = jumlah + i
    i = i + 1

print(f"jumlahnya adalah = {jumlah}")

## LATIHAN LOOPING ##

sisi = 5

# menggunakan for

print(5*"-")
print("awal for")
print(5*"-")

count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print(5*"-")
print("akhir for")
print(5*"-")
print("\n")

# menggunakan while

print(5*"-")
print("awal while")
print(5*"-")

count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print(5*"-")
print("akhir while\n")
print(5*"-")

##############################

## NESTED LOOP
print(5*"=" + "Nested Loop 1" + 5*"=")

for i in range(6):
    for j in range(1,11):
        print(j, end=" ")
    print()

print(5*"=" + "Nested Loop 2" + 5*"=")
for baris in range(5):
  for kolom in range(7):
    print('o', end=" ")
  else:
    print('')






