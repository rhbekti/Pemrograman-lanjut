# diskon.py
totalBelanja = int(input("total belanja : Rp "))
bayar = totalBelanja
# cek diskon dan bonus
if totalBelanja > 100000:
    print("Anda mendapat bonus minuman dingin")
    print("dan diskon 5%")

    # hitung diskon
    diskon = totalBelanja * 5/100 # 5%
    bayar = totalBelanja - diskon

# cetak struk
print("total yang harus dibayar : Rp %s"%bayar)
print("Terima kasih sudah berbelanja")
print("Kami tunggu kedatangannya ...")