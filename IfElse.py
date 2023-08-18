## IF & ELSE STATEMENT ##

"""
1. If statement
2. Kondisinya (boolean)
3. Aksi yang dieksekusi

"""

#If-Else Inline
nama = input("Masukkan nama anda: ")

if nama == "Eka": print("You're doing good!")
print("Akhir dari program")

# If-Else with indentation
umur = int(input("Masukkan umur anda: "))

if umur >= 18:
    print("You're not a minor")
else:
    print("You're a minor")


## ELIF STATEMENT ##

"""
1. Jika kondisi1 bernilai true, blok kode 1 dijalankan.
2. Jika kondisi1 dievaluasi menjadi false, maka kondisi2 dievaluasi.
    2.1. Jika kondisi2 adalah true, blok kode 2 dijalankan.
    2.2. Jika kondisi2 adalah false, blok kode 3 dijalankan.

"""

number = int(input("Insert the number : "))

if number == 0:
    print("It's Zero")
elif number > 0:
    print("Positive Number")
else:
    print("Negative Number")


## Latihan Kalkulator Sederhana ##
print(20*"-")
print("Kalkulator Sederhana")
print(20*"-")

num1 = float(input("Masukkan angka pertama : "))
operator = input("Masukkan operator (+, -, x, /) : ")
num2 = float(input("Masukkan angka kedua : "))

if operator == "+":
    hasil = num1 + num2
    print(f"Hasilnya adalah : {hasil}")
elif operator == "-":
    hasil = num1 - num2
    print(f"Hasilnya adalah : {hasil}")
elif operator == "x":
    hasil = num1 * num2
    print(f"Hasilnya adalah : {hasil}")
elif operator == "/":
    hasil = num1 / num2
    print(f"Hasilnya adalah : {hasil}")
else:
    print("Operator yang anda masukkan salah!")


