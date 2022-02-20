# penjualan toko
namaBarang = input("Masukkan nama barang = ")
hargaBarang = int(input("Masukkan harga barang = "))
jumlahBarang = int(input("Masukkan jumlah barang = "))
# menghitung total bayar
totalBayar = hargaBarang * jumlahBarang
print("--------------------\nNama Barang = "+namaBarang+"\nHarga Barang = "+str(hargaBarang)+"\nJumlah Barang = "+str(jumlahBarang)+"\nTotal bayar anda : ",totalBayar)
bayar = int(input("Masukkan jumlah uang bayar = "))
transaksi = bayar - totalBayar    
# validasi pembayaran
if(transaksi < 0):
    print("Transaksi Sukses,Pembayaran anda kurang "+str(transaksi))
elif(transaksi > 0):
    print("Transaksi Sukses,Uang kembali anda : "+str(transaksi))
else:
    print("Transaksi Sukses")
