## REGULAR EXPRESSION ##

"""

Digunakan ketika kita ingin
mencari bagian spesifik (substring)
pada sebuah string secara lebih
kompleks. -> Mencari pattern

"""

# python built-in regex module
import re
s = "bla456bla"

# re.search(<regex>, <string>)
find = re.search("456", s)

if find:
    print("found!")
else:
    print("Not found!")


# Jika tidak ditemukan -> return None
find_other = re.search("123", s)
print(find_other) #None

# Range characters - ditemukan
find = re.search("[0-9][0-9][0-9]", s)
print(find)

# Range characters - tidak ditemukan
string = "bla12bla"
find = re.search("[0-9][0-9][0-9]", string)
print(find) # None

# Range characters
cari = "the color is grey"
# Mencari substring gray/grey
x = re.search("gr[ae]y", cari)
print(x)

# Latihan
find = 'bla3Bla'
x = re.search("[A-z][0-9][A-z]", find)
print(x) # match -> a3B

# Negasi -> mencari karakter selain yg telah ditentukan
stri = "bla3Bl!!aa"
findstr = re.search("[^0-9A-z][^0-9A-z][0-9A-z]", stri)
print(findstr) # match -> !!a

# Dot -> mencocokkan karakter apapun kecuali baris baru
stri = "bl!3BM"
findstr = re.search(".[^0-9A-z]..", stri)
print(findstr) # match -> l!3B

text = "First line.\nSecond line."
matches = re.findall(r".", text)
print("Matches:", matches) #\n tidak akan terbaca

# Backslash -> mencari literal karakter

"""
Pada contoh berikut, kita akan
mencari titik (.), krn titik
merupakan salah satu operator
pada regex, kita gunakan backlash
agar engine regex tidak menjadikan
titik sebagai operator (melainkan
sebagai sebuah karakter yang dicari)
"""
stri = "its okay."
findstr = re.search("\.", stri)
print(findstr) # match -> .


# REGEX METACHARACTER ##

# \A -> return match jika pola ditemukan pada awal string
test_string = "Hello World!"
find = re.search("\AHello", test_string)
print(find) 

# \b -> return match jika pola ditemukan pada awal atau akhir string
test_string = "hey ho" # test diawal string
find = re.search(r"\bhey", test_string)
print(find)

test_string = "ho hey" # test diakhir string
find = re.search(r"\bhey", test_string)
print(find)

# \B -> return match jika pola ditemukan BUKAN pada awal atau akhir string
test_string = "at, cat, hat, mat"
matches = re.search(r'\Bat', test_string)
print(matches)

# \d -> digit character, shorthand for [0-9]
string = "bla123bla"
find = re.search("\d\d\d", string)
print(find) # match -> 123

# \D -> return match untuk karakter apapun selain digit
test_string = "Umur saya 17 tahun"
matches = re.findall(r'\D', test_string)
print(matches)

# \s -> whitespace/spasi
string = "bla 123 bla"
find = re.findall("\s", string)
print(find)

# \S -> return match untuk karakter apapun selain spasi
test_string = "Umur saya 17 tahun"
matches = re.findall(r'\S', test_string)
print(matches)

# \w -> shorthand for [A-Za-z0-9_]
string = "@93h h7_Y ikkp"
find = re.search("\w\w\w\w", string)
print(find) # match -> h7_Y

# \W -> return match untuk karakter selain alfanumerik dan _
string = "@93h h7_Y ikkp"
find = re.search("\W", string)
print(find)

# \Z -> mengecek pola dimulai dari akhir string, jika sesuai maka mereturn match
test_string = "Hello, World! This is the end"
matches = re.search(r'end\Z', test_string)
print(matches)

# ^ -> start of string
string = "Pinjam dulu 100"
find = re.search("^[A-z]", string)
print(find) # match -> P

# $ -> end of string
string = "Pinjam dulu 100"
find = re.search("[0-9][0-9][0-9]$", string)
print(find) # match -> 100


## REGEX QUANTIFIER ##

"""
Quantifier : mencari jumlah karakter

"""

# * -> zero or more
s1 = "ct"
s2 = "cat"
s3 = "caaaaaat"

"""
Mencari berapa jumlah a 
yang berada setelah c dan
sebelum t 

"""
print(re.search("ca*t", s1))
print(re.search("ca*t", s2))
print(re.search("ca*t", s3)) 

# + -> one or more
s1 = "ct"
s2 = "cat"
s3 = "caaaaaat"

"""
Mencari berapa jumlah a 
yang berada setelah c dan
sebelum t (a minimal ber-
jumlah 1)

"""
print(re.search("ca+t", s1)) # None
print(re.search("ca+t", s2))
print(re.search("ca+t", s3)) 

# ? -> zero or one
s1 = "color"
s2 = "colour"
s3 = "colouur"
print(re.search("colou?r", s1))
print(re.search("colou?r", s2))
print(re.search("colou?r", s3)) # None krn u lebih dari 1

# {} -> {m, n} or {m}
s1 = "coloor"
s2 = "coloooor"
s3 = "color"
print(re.search("colo{2,4}r", s1))
print(re.search("colo{2,4}r", s2))
print(re.search("colo{2,4}r", s3)) # None
print(re.search("colo{2}r", s1))

# | -> sama seperti operator OR
test_string = "The color of the car is either blue or red."
matches = re.findall(r'blue|red', test_string)
print(matches)

## REGEX GROUPING ##

# () -> grouping

"""

cat+ hanya mencari berapa
kali jumlah t muncul dalam
string, sedangkan (cat)+ 
mencari berapa kali jumlah
semua karakter yg ada dalam 
kurung (cat) muncul

"""
str1 = "cattt"
str2 = "catcatcat"
print(re.search("cat+", str1)) # match -> cattt
print(re.search("cat+", str2)) # match -> cat
print(re.search("(cat+)", str1)) # match -> cat
print(re.search("(cat+)", str2)) # match -> catcatcat

# Contoh Lain
str1 = "Feb 2022"
str2 = "February 2022"
str3 = "Feby 2022"

print(re.search('Feb(ruary)? 2022', str1))
print(re.search('Feb(ruary)? 2022', str2))
print(re.search('Feb(ruary)? 2022', str3)) # None -> krn hanya ada y yg muncul, bukan ruary scr keseluruhan

#re.findall -> mencari semua pattern yg match
teks = "In 1908, Budi Utomo was formed. The Youth Pledge was declared in 1928. Indonesia declared independence in 1945"

"""
Mencari semua digit yang muncul
pada teks. Digit tsb hrs memiliki
panjang 4 karakter

"""
print(re.findall("\d{4}", teks)) # match -> [1908, 1928, 1945]

#re.split -> membagi sebuah string menjadi bagian kecil berdasarkan pola yg ditentukan
text = "agar silaturahmi tidak terputus, pinjam dulu seratus"
words = re.split(r'\s', text)
print(words)

#re.sub -> mengganti string yang match dgn string yang diberikan
print(re.sub("\d{4}", "YEAR", teks))

#re.subn -> 
pattern = '\s'
replace = '@'
# variabel count merupakan unpacking pada tuple
new_string, count = re.subn(pattern, replace, text)
print(new_string)
print("Jumlah pergantian : ", count)

#re.match 
"""
Mencari sebuah pattern dimulai
dari karakter pertama pada string.
Jika karakter pertama tidak memenuhi
pola, maka langsung mereturn none.
Namun, jika karakter pertama memenuhi
maka akan dilanjutkan pengecekan pola
hingga selesai

"""
pattern = "a...s$"
test_string = "abyss"
result = re.match(pattern, test_string)
print(result) # Match 

pattern = "a...s$"
test_string = "in a abyss"
result = re.match(pattern, test_string)
print(result) # None -> mulai dari karakter pertama tidak terpenuhi
















