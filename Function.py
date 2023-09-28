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

##############################################


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

##############################################

# *args pada fungsi

"""
*args digunakan ketika ingin
membuat function yang akan digunakan
berulang kali. Dimana setiap kali
function itu digunakan, function tsb
cenderung memiliki parameter yang berbeda
"""

def fungsi(nama, tinggi, berat):
    print(f"{nama} memiliki tinggi badan {tinggi} cm dan berat badan {berat} kg")
fungsi("Kamu", 170, 40)

def function(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} memiliki tinggi badan {tinggi} cm dan berat badan {berat} kg")
function(["Kamu", 170 , 20])

def function(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} memiliki tinggi badan {tinggi} cm dan berat badan {berat} kg")
function("Kamu", 170 , 30)

# Studi Kasus
def tambah(*data):
    output = 0
    for angka in data:
        output = output + angka
    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"Hasilnya adalah : {hasil}")

hasil = tambah(10, 20, 5)
print(f"Hasilnya adalah : {hasil}")

# ##############################################

# *kwargs pada fungsi

"""
kwargs menyimpan arguments 
dalam bentuk dictionary

"""

contohDict = {
    "nama" : "Eka",
    "tinggi" : 160,
    "berat" : 50
}
print(contohDict["nama"])

def function(**kwargs):
    name = kwargs["nama"]
    height = kwargs["tinggi"]
    weight = kwargs["berat"]
    print(f"{name} memiliki tinggi badan {height} cm dan berat badan {weight} kg")

function(nama="Kamu", tinggi="150", berat="20")

# Studi Kasus

def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output +=angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("tidak ada operasi yang tersedia")

    return output

hasil = math(1,2,3,4, option="tambah")
print(f"hasil jumlah = {hasil}")

hasil = math(1,2,3,4, option="kali")
print(f"hasil kali = {hasil}")

##############################################

# Type Hints Pada Fungsi

"""
Digunakan untuk memudahkan
dalam memahami kode

"""

# bentuk standar fungsi yang udah kita pelajari

'''
studi kasus
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)

fungsi(1)
fungsi("Eka")
fungsi

'''

def sepuluh_pangkat(argument:int) -> int:
    output = 10**argument
    return output

HASIL = sepuluh_pangkat(2)
print(HASIL)


