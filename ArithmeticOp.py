## OPERASI ARITMATIKA ##

a = 10
b = 3

# Operasi Penjumlahan (+)
hasil = a + b
print(a, "+", b, "=", hasil)

# Operasi Pengurangan (-)
hasil = a - b
print(a, "-", b, "=", hasil)

# Operasi Perkalian (*)
hasil = a * b
print(a, "*", b, "=", hasil)

# Operasi Penjumlahan (/)
hasil = a / b
print(a, "/", b, "=", hasil)

# Operasi Eksponen/Perpangkatan (**)
hasil = a ** b
print(a, "**", b, "=", hasil)

# Operasi Modulus (%)
hasil = a % b
print(a, "%", b, "=", hasil)

# Operasi Floor Division (//)
hasil = a // b
print(a, "//", b, "=", hasil)

## PRIORITAS OPERASI / OPERATIONAL PROCEDURE ##
"""
    1. Tanda kurung ()
    2. Eksponen **
    3. Perkalian dkk * / ** % //
    4. Penjumlahan & Pengurangan + -
"""

## Latihan Operasi Aritmatika ##

# Konversi dari Celcius ke satuan lainnya #
celcius = float(input("Masukkan suhu dalam celcius : "))
print("Suhu saat ini adalah", celcius, " Celcius")

## Reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah", reamur, " Reamur")

## Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah", fahrenheit, " Fahrenheit")

##Kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah", kelvin, " Kelvin")


### TUGAS ###
# Konversi fahrenheit ke kelvin
fahrenheit = float(input("Masukkan suhu dalam fahrenheit : "))
print("Suhu saat ini adalah", fahrenheit, " Fahrenheit")

kelvin = (5/9) * (fahrenheit - 32) + 273
print("Suhu dalam kelvin adalah", kelvin, " Kelvin")

#Konversi kelvin ke fahrenheit
kelvin = float(input("Masukkan suhu dalam Kelvin : "))
print("Suhu saat ini adalah", kelvin, " Kelvin")

fahrenheit = (9/5) * (kelvin - 273) + 32
print("Suhu saat ini adalah", fahrenheit, " Fahrenheit")














