#median.py
jmlSiswa = int(input("Masukan jumlah siswa ? "))
nilai = []
for i in range(jmlSiswa):
    x = int(input("Masukan nilai siswa = "))
    nilai.append(x)
#Mencari median atau nilai tengah
nilai.sort()
lokMedian=0;
if (jmlSiswa%2==1):
    lokMedian = int((jmlSiswa+1)/2)
else:
    lokMedian =int(1/2*(jmlSiswa/2+((jmlSiswa/2)+1)))
#output
print(nilai)
print(" median = ", nilai[lokMedian])