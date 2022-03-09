# tertinggi.py
jmlSiswa = int(input("Masukan jumlah siswa ? "))
nilai=[]
for i in range(jmlSiswa):
    x = int(input("Masukan nilai siswa = "))
    nilai.append(x)
    min = x
for n in nilai:
    if min > n:
        min = n
# output
print(min)