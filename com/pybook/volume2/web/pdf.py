import requests
import sys

base_url = 'http://subeen.com/download/'

info_dt = {'name': 'Subeen', 'email': 'book@subeen.com', 'country': 'Bangladesh'}

url = base_url + 'process.php'

res = requests.post(url, data=info_dt)

if res.ok is False:
    sys.exit('Error downloading the file')

with open('D:\\$@q!b\\Files\\Java\\pydownloads\\cpbook.pdf', 'wb') as pdf:
    pdf.write(res.content)

print('Download complete!')
