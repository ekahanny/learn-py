## CONTINUE, PASS, & BREAK ##

# PASS #

"""
Statement pass berguna sebagai placeholder 
untuk suatu fungsi atau suatu class yang 
belum kita implementasikan secara nyata.
Gunakan pass ketika belum diberi implementasi
agar interpreter python tidak menampilkan error

"""

for i in range(5):
  pass # sebelum diberi implementasi


# CONTINUE #

"""
Statement continue akan melewati 
proses iterasi & langsung menuju 
pada step selanjutnya.

"""
print("--- CONTINUE 1 ---")
angka = 0
while angka < 5:
    angka += 1
    print(f"angka sekarang bernilai : {angka}") #aksi 1

    if angka == 3:
        print("kondisi tertentu")
        continue

    print("looping berlanjut") # aksi 2

print("Looping berhenti\n")


print("--- CONTINUE 2 ---")
i = 0

while i < 10:

    i = i + 1
    if (i % 2) == 0:
        continue
    print(i)
print()

"""
pada implementasi kode diatas, statement 
continue akan melewati aksi 2 dan langsung 
lanjut ke looping setelahnya

"""

# BREAK #

"""
Statement break akan langsung
menghentikan proses iterasi.

"""
print("--- BREAK 1 ---")

data_int = int(input("hitung sampai :\t"))
angka = 0

while True:
    angka += 1
    print(f"count : {angka}")

    if angka == data_int:
        print("perhitungan berakhir")
        break
    
    print("looping berlanjut")

print("looping berhenti\n")


print("--- BREAK 2 ---")
i = 1

while i <= 5:
    print(i)
    if i == 3:
        break
    i = i + 1




