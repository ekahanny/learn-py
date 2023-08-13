## INPUT DATA ##
# Untuk mengambil sebuah inputan, kita gunakan sintaks input

data = input("Masukkan data : ")
print("data =", data, ", bertipe = " , type(data)) 
#default data inputan akan bertipe string

#untuk mengubah tipe data dari nilai input, dilakukan casting:
data_int = int(input("Masukkan bilangan bulat : "))
print("data =", data_int, ", bertipe = ", type(data_int))

data_float = float(input("Masukkan bilangan desimal : "))
print("data =", data_float, ", bertipe = ", type(data_float))


# khusus untuk boolean, data inputan harus dicast ke int terlebih dahulu
data_bool = bool(int(input("Masukkan nilai boolean : ")))
print("data =", data_bool, ", bertipe = " , type(data_bool)) 
