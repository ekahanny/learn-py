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

print(5*"=" + "While Loop" + 5*"=")
i = 0

while i < 5:
    i += 1
    print(i)


