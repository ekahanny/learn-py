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

# cara return 1
x = fungsi_kuadrat(2)
print(x)

# cara return 2
print(fungsi_kuadrat(3))

# cara return 3 -> menambahkan dgn variabel lain
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

print(f"Hasil tambah : {a}")
print(f"Hasil kurang : {b}")
print(f"Hasil kali : {c}")
print(f"Hasil bagi : {d :.2f}")





