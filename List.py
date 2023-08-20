## LIST ##

"""
Pada python, sebuah array
disebut sebagai list.

"""

# list dapat berupa gabungan beberapa tipe data
ini_list = [1, "satu", True, 2, "dua", False] 
print(ini_list)

# cara alternatif membuat list
data_range = range(0, 10, 2) # start, stop, step
data_list = list(data_range) # menggunakan keyword list
print(data_list)

# membuat list dengan for loop
list_dgn_for = [i**2 for i in range(0, 10)] # di pangkat 2
print(list_dgn_for)

# membuat list dengan for loop dan if
list_dgn_for_if = [i for i in range(0, 10) if i != 5] # skip 5
print(list_dgn_for_if)

list_dgn_for_if = [i for i in range(0, 10) if i % 2 == 0] # genap
print(list_dgn_for_if)

list_dgn_for_if = [i for i in range(0, 10) if i % 2 != 0] # ganjil
print(list_dgn_for_if)