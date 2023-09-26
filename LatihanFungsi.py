## PROGRAM MENGHITUNG LUAS & KELILING PERSEGI PANJANG ##

import os

def header():
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    lebar = int(input("Masukkan Nilai Lebar : "))
    panjang = int(input("Masukkan Nilai Panjang : "))
    return lebar, panjang

def hitung_luas(lebar, panjang):
    return lebar * panjang

def hitung_keliling(lebar, panjang):
    return 2 * (lebar + panjang)

def display_output(message, value):
    print(f"Hasil Perhitungan {message} Adalah = {value}")

# Program Utama
while True:
    header()
    LEBAR, PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)

    display_output("Luas", LUAS)
    display_output("Keliling", KELILING)

    isLanjut = input("Apakah anda ingin melanjutkan perhitungan? (y/n) : ")

    if isLanjut == "n":
        break

print("Program Selesai, Terima Kasih!")