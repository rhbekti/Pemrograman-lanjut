# urut data
jmlSiswa = int(input("Masukan jumlah siswa ? "))
nilai=[]
for i in range(jmlSiswa):
    x = int(input("Masukan nilai siswa = "))
    nilai.append(x)
nilai.sort()
print(nilai)