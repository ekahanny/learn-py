# a = 10, a adalah sebuah variabel dengan nilai 10


""" TIPE DATA """

# tipe data integer (bilangan bulat)
data_int = 1
print("data :" , data_int, ", bertipe : ", type(data_int))

# tipe data float (bilangan desimal)
data_float = 1.5
print("data :" , data_float, ", bertipe : ", type(data_float))

# tipe data string (kumpulan karakter)
data_str = "Ini adalah string"
print("data :" , data_str, ", bertipe : ", type(data_str))

# tipe data boolean (True or False)
data_bool = True
print("data :" , data_bool, ", bertipe : ", type(data_bool))

### TIPE DATA KHUSUS

# tipe data kompleks
data_complex = complex(5, 6) #5 adalah bil. real, 6 adalah bil. imajiner
print("data :" , data_complex, ", bertipe : ", type(data_complex))

# tipe data dari bahasa c
from ctypes import c_double

data_c_double = c_double(10.5)
print("data :" , data_c_double, ", bertipe : ", type(data_c_double))



""" CASTING TIPE DATA """
# Casting = mengubah satu tipe data ke tipe data lainnya


## INTEGER
print("=== INTEGER ===")
data_int = 9
print("data :" , data_int, ", bertipe : ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika nilai int = 0
print("data :" , data_float, ", setelah dicasting bertipe : ", type(data_float))
print("data :" , data_str, ", setelah dicasting bertipe : ", type(data_str))
print("data :" , data_bool, ", setelah dicasting bertipe : ", type(data_bool))


## FLOAT
print("=== FLOAT ===")
data_float = 9.9
print("data :" , data_float, ", bertipe : ", type(data_float))

data_int = int(data_float) #akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float)
print("data :" , data_int, ", setelah dicasting bertipe : ", type(data_int))
print("data :" , data_str, ", setelah dicasting bertipe : ", type(data_str))
print("data :" , data_bool, ", setelah dicasting bertipe : ", type(data_bool))


## BOOLEAN
print("=== BOOLEAN ===")
data_bool = True
print("data :" , data_bool, ", bertipe : ", type(data_bool))

data_int = int(data_bool) 
data_str = str(data_bool)
data_float = float(data_bool)
print("data :" , data_int, ", setelah dicasting bertipe : ", type(data_int))
print("data :" , data_str, ", setelah dicasting bertipe : ", type(data_str))
print("data :" , data_float, ", setelah dicasting bertipe : ", type(data_float))


## STRING
print("=== STRING ===")
data_str = "10"
print("data :" , data_str, ", bertipe : ", type(data_str))

data_int = int(data_str) #string harus angka
data_float = float(data_str) #string harus angka
data_bool = bool(data_str) #akan bernilai false jika string kosong
print("data :" , data_int, ", setelah dicasting bertipe : ", type(data_int))
print("data :" , data_float, ", setelah dicasting bertipe : ", type(data_float))
print("data :" , data_bool, ", setelah dicasting bertipe : ", type(data_bool))




















