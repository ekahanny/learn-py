## MENDUPLIKAT LIST ##

a = ["Hanny", "Eka", "Oktavia"]

print("Sebelum Diubah")
print(f"a = {a}")

b = a # pass by reference
print(f"b = {b}")

# mengubah elemen list a dan b
a[1] = "Ekuy"
b.sort()
print("Setelah Diubah")
print(f"a = {a}")
print(f"b = {b}")

"""

jika kita menduplikat list
menggunakan pass by reference,
maka list tersebut akan memiliki 
address yang sama sehingga ketika
dilakukan perubahan pada salah
satu list, list yang terduplikat
juga akan ikut berubah

"""

# address dari kedua list a dan b sama
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# menduplikat list dengan copy

"""

jika menggunakan .copy, maka list
yang terduplikat memiliki address
yg berbeda. 

"""
print("membuat list c dengan a.copy()\n")
c = a.copy() # full duplikat / data baru

print("Sebelum diubah")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

# mengubah elemen list c
c[0] = "Eka"
print("Setelah diubah")
# data a dan b tidak ikut berubah
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")