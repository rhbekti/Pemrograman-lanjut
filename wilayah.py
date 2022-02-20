# program informasi provinsi di indonesia
# import library request
import requests
# mengambil data dari api
response = requests.get("https://dev.farizdotid.com/api/daerahindonesia/provinsi")
# menyimpan respon dalam bentuk json
data = response.json()
# menampilkan data provinsi
print("Nama Provinsi")
print("---------------------")
for provinsi in data['provinsi']:
    print(provinsi['nama'])
