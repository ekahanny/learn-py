## TUTORIAL MEMBACA FILE EKSTERNAL ##

print(3*"=", " MEMBACA FILE TXT", 3*"=")
file = open("text.txt", mode="r")

# membaca seluruh file
print(file.read())

# membaca per baris
print(file.readline(), end="") # baca baris pertama
print(file.readline(), end="") # baca baris kedua

# membaca semua baris menjadi list
print(file.readlines())

# file yang terbuka harus ditutup
file.close()

# gunakan with jika ingin membuka file & terclose otomatis
with open("text.txt", mode="r") as file:
    content = file.readline()
    print(content)

print(f"apakah file sudah terclose? : {file.closed}")

## TUTORIAL WRITE FILE EKSTERNAL ##

# Mode Write #

"""

Akan membuat file baru jika file
belum ada, kemudian akan overwrite
(menghapus isinya & mengganti yang
 baru) isi dari file jika file sudah 
ada atau sudah terbuat

"""

with open("text.txt", mode="w", encoding="utf-8") as file:
    file.write("Universitas Hasanuddin")

with open("text1.txt", mode="w", encoding="utf-8") as file:
    file.write("Ini akan membuat file baru")


# Mode Append #

"""

Akan menambahkan semua 
konten yang telah tertulis
pada file yang ditentukan

"""

with open("text.txt", mode="a", encoding="utf-8") as file:
    file.write("Sistem Informasi\n")

with open("text.txt", mode="a", encoding="utf-8") as file:
    file.write("Departemen Matematika\n")

# Mode r+ #

"""

Dapat membuka file yang ada,
kemudian akan menimpa isi/konten
dari file tersebut

"""

with open("text.txt",'r+',encoding="utf-8") as file:
    file.write("baris-1 \n") # menimpa isi text sesuai dengan panjang data
    file.write("baris-2 \n")
    file.write("baris-3 \n")

with open("text.txt",'r+',encoding="utf-8") as file:
    data = file.read()
    print(data)