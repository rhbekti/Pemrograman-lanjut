jumlahPositif = 0
jumlahNegatif = 0

banyakInput = 5
i = 1

while i <= 5:
    bil = int(input("Masukkan bilangan = "))
    if(bil > 0):
        print("Bilangan Positif")
        jumlahPositif = jumlahPositif + bil
    else:
        print("Bilangan Negatif")
        jumlahNegatif = jumlahNegatif + bil
    i = i + 1
print(jumlahPositif)
print(jumlahNegatif)