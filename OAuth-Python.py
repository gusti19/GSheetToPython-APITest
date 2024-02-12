!pip install gspread

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Tentukan kredensial
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('[YOUR_FILE.json]', scope)
client = gspread.authorize(creds)

# Buka spreadsheet berdasarkan ID
spreadsheet = client.open_by_key('d/[THIS LINK]/edit')

# Pilih lembar (sheet) yang diinginkan
sheet = spreadsheet.worksheet('Sheet X')

# Ambil data dari cell tertentu
cell_values = sheet.range('X1:X2')

# Tampilkan nilai dari cell tertentu
for cell in cell_values:
    print(cell.value)
