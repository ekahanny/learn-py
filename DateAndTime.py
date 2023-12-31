## DATE AND TIME (Library) ##

import datetime as dt

print("Silahkan masukkan tanggal lahir anda!")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))

# Format : yyyy/mm/dd
tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda: {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal: {hari_ini}")

umur_hari = hari_ini - tanggal_lahir #akan menghasilkan umur dalam format hari
umur_tahun = umur_hari.days // 365 
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Hari lahir anda adalah : {tanggal_lahir:%A}")
print(f"Umur anda : {umur_tahun} tahun, {umur_bulan_sisa} bulan")
