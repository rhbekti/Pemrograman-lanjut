# rata-rata
jmlSiswa = int(input("Masukan jumlah siswa ? "))
nilai=[]
for i in range(jmlSiswa):
    x = int(input("Masukan nilai siswa = "))
    nilai.append(x)

rataRata = sum(nilai)/jmlSiswa
print(rataRata)