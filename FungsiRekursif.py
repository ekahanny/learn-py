"""
Fungsi rekursif dapat memanggil 
dirinya sendiri. Fungsi rekursif
dapat dianalogikan sebagai looping

"""

# def fungsiRekursif():
#     print("Pinjam dulu 100")
#     fungsiRekursif()

# # fungsi ini akan dilakukan berulang tanpa henti
# fungsiRekursif() 

"""
Fungsi rekursif terdiri dari 2 bagian
1. Bagian yang memanggil dirinya sendiri (Rekurens)
2. Bagian pengecekan kondisi utk berhenti (Stopping Criteria)

"""

# Contoh 1
def factorial(n):
    if n == 1: # stopping condition
        return 1
    else:
        return n*factorial(n-1) # rekurens

x = factorial(5)
print(f"Hasil Faktorial : {x}" )

# Contoh 2
def show_intervals(mulai, akhir):
    print(mulai, end=" ")
    mulai += 1
    if mulai <= akhir: # stopping condition
        show_intervals(mulai, akhir) # rekurens

show_intervals(1,10)

# Contoh Tanpa Stopping Condition
def show_multiple(value):
    print(value, end=" ")
    value += value
    show_multiple(value)

show_multiple(2)

    
