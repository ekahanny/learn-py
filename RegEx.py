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


## REGEX METACHARACTER ##

# \d -> digit character, shorthand for [0-9]
string = "bla123bla"
find = re.search("\d\d\d", string)
print(find) # match -> 123

# \w -> shorthand for [A-Za-z0-9_]
string = "@93h h7_Y ikkp"
find = re.search("\w\w\w\w", string)
print(find) # match -> h7_Y

# \s -> whitespace/spasi
string = "bla 123 bla"
find = re.search("\s", string)
print(find)

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


#re.sub -> mengganti string yang match dgn string yang diberikan
print(re.sub("\d{4}", "YEAR", teks))















