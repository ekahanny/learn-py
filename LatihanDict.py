import datetime
import os
import random
import string

data_template = {
    'nama' : 'nama',
    'nim' : 000000,
    'prodi' : 'prodi',
    'sks_lulus' : 'sks_lulus',
    'ttl' : datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

os.system("cls")
print(f"{'SELAMAT DATANG' :^20}")
print(f"{'DATA MAHASISWA' :^20}")
print("-"*20)

"""
Memasukkan hasil input 
kedalam dictionary kosong 
dgn menggunakan key pada 
dict template

"""
while True:
    mahasiswa = dict.fromkeys(data_template.keys()) 
    mahasiswa['nama'] = input('Nama Mahasiswa : ')
    mahasiswa['nim'] = input('NIM : ')
    mahasiswa['prodi'] = input('Prodi : ')
    mahasiswa['sks_lulus'] = int(input('SKS Dilulusi : '))
    TAHUN_LAHIR = int(input('Tahun Lahir (YYYY): '))
    BULAN_LAHIR = int(input('Bulan Lahir (1-12): '))
    TANGGAL_LAHIR = int(input('Tanggal Lahir (1-31): '))
    mahasiswa['ttl'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    """
    Menggenerate random key
    dengan memilih string 
    uppercase sebanyak 6 
    """
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS Lulus':<10} {'Tanggal Lahir':<10}")
    print('-'*60)

    for mahasiswa in data_mahasiswa:
	    KEY = mahasiswa
		
	    NAMA = data_mahasiswa[KEY]['nama']
	    NIM = data_mahasiswa[KEY]['nim']
	    SKS = data_mahasiswa[KEY]['sks_lulus']
	    LAHIR = data_mahasiswa[KEY]['ttl'].strftime("%x")
		
	    print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")

    print("\n")
    is_done = input("Tambahkan data? (y/n) : ")

    if is_done == "n":
        break

print("TERIMA KASIH")




