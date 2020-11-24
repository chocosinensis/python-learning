import requests

img_url = 'https://cdn.pixabay.com/photo/2019/10/29/14/46/landscape-4587079__340.jpg'

res = requests.get(img_url)

with open('D:\\$@q!b\\Files\\Java\\pydownloads\\Nature.jpg', 'wb') as pic:
    pic.write(res.content)
