## FUNGSI ##

"""
Pada python, pemanggilan fungsi
harus setelah fungsi tsb dibuat

"""


##############################################


# Fungsi Dengan Argument/Parameter


# Fungsi Tambah
def tambah(angka1, angka2):
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

tambah(1,2)

# Fungsi Say Hi
def say_hi(list_peserta):
    """
    gunakan .copy agar 
    tdk mengganggu list
    nama_peserta yang 
    berada diluar function

    """
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Halo, {peserta}!")

nama_peserta = ["Eka", "Hanny", "Oktavia"]

# nama_peserta menggantikan parameter list_peserta
say_hi(nama_peserta) 


##############################################


# Fungsi Dengan Kembalian (Return)

def fungsi_kuadrat(input_angka):
    output_kuadrat = input_angka**2
    return output_kuadrat

# cara 1
x = fungsi_kuadrat(2)
print(x)

# cara 2
print(fungsi_kuadrat(3))

# cara 3 -> menambahkan dgn variabel lain
y = 10 + fungsi_kuadrat(7)
print(y)

# Fungsi Dengan Multiple Return
def operasi_aritmatika(operand1, operand2):
    tambah = operand1 + operand2
    kurang = operand1 - operand2
    kali = operand1 * operand2
    bagi = operand1 / operand2

    return tambah, kurang, kali, bagi

a,b,c,d = operasi_aritmatika(7,3)

print(f"Hasil tambah. : {a}")
print(f"Hasil kurang : {b}")
print(f"Hasil kali : {c}")
print(f"Hasil bagi : {d :.2f}")



##############################################

# Fungsi Dengan Default Argument

"""

1. def fungsi (argument)
2. def fungsi (argument = nilai default)

"""

# Contoh 1
def greet(name = "Guest"):
    print(f"Hello, {name}!")

greet() # akan menggunakan default argument
greet("John Doe")

# Contoh 2
def greeting_message(name, message="Apa Kabar?"):
    print(f"Halo, {name}. {message}")

greeting_message("Eka", "Selamat Pagi!") #default argument pada message akan terganti
greeting_message("Hanny") #inputan biasa pada name, sedangkan name menggunakan default argument

# Contoh 3
def hitung_pangkat(angka, pangkat=2):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2,4)) # Output 1

# Keyword/Named Arguments

'''
kita bisa mengisi parameter fungsi 
tanpa mengikuti urutan yang ditentukan 
pada suatu fungsi, sebutkan saja 
parameter & valuenya
'''
hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil) # Output 2

# contoh 4
def fungsi_tambah(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi_tambah()) #10
print(fungsi_tambah(input3=10)) #17


