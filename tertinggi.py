# tertinggi.py
jmlSiswa = int(input("Masukan jumlah siswa ? "))
nilai=[]
for i in range(jmlSiswa):
    x = int(input("Masukan nilai siswa = "))
    nilai.append(x)
    max = 0
for n in nilai:
    if max < n:
        max = n
# output
print(max)