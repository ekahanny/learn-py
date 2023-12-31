# ## STRING ##

data = "ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \ (backlash)

"""
backlash merupakan special character 
yang dapat memberitahu interpreter
untuk mengubah tanda ' menjadi string
"""

print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("C:\\user\\Ucup")

# tab = menambahkan spasi
print("string ini akan memiliki \t\tspasi yang berjauhan")

# backspace = menghilangkan spasi
print("tidak \bada \bspasi")

# newline
print("baris pertama.\nbaris kedua.") # LF -> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR -> carriage return -> commodore, acorn, lisp 
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return -> dipakai oleh windows

# 3. String literal atau raw

# hati-hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Eka Hanny
Kelas : XII MIPA 1   
""")

# multiline literal string dan RAW
print(r"""
Nama : Ucup
Kelas : XII MIPA\1
Website : www.test.com/newID
""")

## OPERASI DAN MANIPULASI STRING ###

# 1. Menyambung String (concatenate)
nama_pertama = "Eka"
nama_tengah = "Hanny"
nama_akhir = "Oktavia"

nama_lengkap = nama_pertama + nama_tengah + nama_akhir
print(nama_lengkap)

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print("panjang " + nama_lengkap + " adalah " + str(panjang))

# 3. operator untuk string

# cek apakah ada komponen pada sebuah string
a = "a"
status = a in nama_lengkap
print("apakah " + a + " ada di " + nama_lengkap + ", " + str(status))

E = "E"
status = E in nama_lengkap
print("apakah " + E + " ada di " + nama_lengkap + ", " + str(status))

x = "x"
status = x not in nama_lengkap
print("apakah " + x + " tidak ada di " + nama_lengkap + ", " + str(status))

# mengulang string
print("wk"*100)
print(100*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0]) # dimulai dari 0
print("index ke-6 : " + nama_lengkap[6]) # index bebas
print("index ke-(-1) : " + nama_lengkap[-1]) # indexing dari dibelakang
print("index ke-[6,8) : " + nama_lengkap[6:8]) # dimulai dari index 6 sampai sebelum 8
print("index ke-[0,2,4,6,8] : " + nama_lengkap[0:10:2]) # diambil index 0,2,4,6,8

# item paling kecil
print("nilai terkecil : " + min(nama_lengkap))
# item paling besar
print("nilai terbesar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII number dari spasi : " + str(ascii_code))
data = 117
print("Character dari ascii code 117 : " + chr(data))

# 4. operator dalam bentuk method

jumlah = nama_lengkap.count("a")
print("jumlah a di " + nama_lengkap + " : " + str(jumlah))

## merubah case pada string

# merubah semua ke upper case
sapaan = "hallo"
print("normal " + sapaan)
sapaan = sapaan.upper()
print("upper " + sapaan)

# merubah semua ke lower case
sapaan = "hAlLoOOo"
print("normal " + sapaan)
sapaan = sapaan.lower()
print("lower " + sapaan)

## method is, untuk pengecekan

# contoh isupper()
salam = "SIST"
apakah_upper = salam.isupper()
print(salam + " is upper? " + str(apakah_upper))
salam = salam.lower()
apakah_upper = salam.isupper()
print(salam + " is upper? " + str(apakah_upper))

# islower() <- untuk pengecekan apakah lower case semua
# isalpha() <- untuk mengecek apakah huruf semua
# isalnum() <- apakah huruf dan angka
# isdecimal() <- apakah numeric
# isspace() <- apakah isinya spasi, tab dan enter (newline \n)
# istitle() <- huruf pertama setiap kata upper case

judul = "It Is Okay To Not Be Okay"
cek_judul = judul.istitle()
print(judul + " is title? " + str(cek_judul))

# startwith() dan endwith()

cek_start = "Eka Hanny Oktavia".startswith("Eka")
print("start " + str(cek_start))
cek_end = "Eka Hanny Oktavia".endswith("Oktavia")
print("end " + str(cek_end))

# join() dan split()

"""
Menggabungkan elemen dalam array 
dan dipisah sesuai dengan keyword 
yang ada

""" 
pisah = ['Ini','ngetes','doang']
gabungan = ' hehe '.join(pisah)
print(pisah)
print(gabungan)

"""
Memisahkan string menjadi 
elemen-elemen dalam array

"""
gabungan = "naik vespa keliling kota"
pisah = gabungan.split()
print(gabungan)
print(pisah)

"""
Memisahkan string berdasarkan keyword
dan dimasukkan kedalam sebuah array

"""
gabungan = "naikehmvespaehmkelilingehmkota"
pisah = gabungan.split("ehm")
print(gabungan)
print(pisah)

# alokasi karakter
print("'kiri      '")

kanan = "kanan".rjust(20) # rata kanan dengan 20 karakter
print("'" + kanan + "'")

kiri = "kiri".ljust(20) # rata kiri dengan 20 karakter
print("'" + kiri + "'")

tengah ="tengah".center(20) # rata tengah dengan 20 karakter
print("'" + tengah + "'")

tengah ="tengah".center(20,'-') # rata tengah dengan 20 karakter
print("'" + tengah + "'")

# kebalikan dari alokasi karakter
kanan = kanan.strip()
print("'" + kanan + "'")
tengah = tengah.strip('-')
print("'" + tengah + "'")

## STRING WIDTH & ALLIGNMENT ##

# Width and Multiline
data_nama = "Eka Hanny"
data_umur = 20
data_tinggi = 160
data_nomor_sepatu = 41

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"="+"Data String Standard"+5*"=")
print(data_string)

# String multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data String Multiline"+5*"=")
print(data_string)

# String multiline (kutip triplets)
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# mengatur lebar
# tanda >5 berarti memberi jarak ke kanan sebanyak 5
data_string = f"""
nama   = {data_nama:>5} 
umur   = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)