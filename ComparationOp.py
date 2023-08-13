## OPERASI KOMPARASI ##

# Setiap hasil dari operasi komparasi adalah boolean
a = 3
b = 5

## Lebih Besar Dari (>)
print("== Besar Dari ==")
hasil = a > b #False
print(a, ">", b, "=", hasil)
hasil = a > 2 #True
print(a, ">", 2, "=", hasil)

## Kurang Dari (<)
print("== Kurang Dari ==")
hasil = a < b #True
print(a, "<", b, "=", hasil)
hasil = a < 2 #False
print(a, "<", 2, "=", hasil)

## Lebih Besar atau Sama Dengan (>=)
print("== Lebih Besar Dari atau Sama Dengan ==")
hasil = a >= b #False
print(a, ">=", b, "=", hasil)
hasil = a >= 3 #True
print(a, ">=", 2, "=", hasil)

## Kurang Dari atau Sama Dengan (<=)
print("== Kurang Dari atau Sama Dengan ==")
hasil = a <= b #True
print(a, "<=", b, "=", hasil)
hasil = a <= 3 #True
print(a, "<=", 2, "=", hasil)

## Sama Dengan (==)
print("== Sama Dengan ==")
hasil = a == b #False
print(a, "==", b, "=", hasil)
hasil = a == 3 #True
print(a, "==", 2, "=", hasil)

## Tidak Sama Dengan (!=)
print("==  Tidak Sama Dengan ==")
hasil = a != b #True
print(a, "!=", b, "=", hasil)
hasil = a != 3 #False
print(a, "!=", 2, "=", hasil)

# IS & IS NOT sebagai komparasi object identity/variabel
print("== Object Identity (IS & IS NOT) ==")
x = 5
y = 5
z = 6
# untuk mengecek id dari variabel di dalam memori, gunakan:
print("nilai x = ", x, " ,id = ", hex(id(x)))
print("nilai y = ", y, " ,id = ", hex(id(y)))
print("nilai z = ", z, " ,id = ", hex(id(z)))

hasil = x is y #True
print("x is y = ", hasil)
hasil = y is z #False
print("y is z = ", hasil)
hasil = x is not z #True
print("x is z = ", hasil)














