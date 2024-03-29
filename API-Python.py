import requests

# Tentukan kunci API
api_key = 'API-mu dewe lah'

# URL untuk mengambil data dari spreadsheet
url = f"https://sheets.googleapis.com/v4/spreadsheets/BLABLABLA/values/Number!A1:B2?key={api_key}"

# Lakukan permintaan GET untuk mendapatkan data
response = requests.get(url)

# Jika respons berhasil (kode status 200), tampilkan nilai dari cell
if response.status_code == 200:
    data = response.json()
    values = data.get('values', [])
    for row in values:
        print(row)
else:
    print("Gagal mengambil data:", response.text)
