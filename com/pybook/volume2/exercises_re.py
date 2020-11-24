import re  # Ch 7

with open('D:\\$@q!b\\Files\\Java\\exer_re.txt', 'r') as fr:  # Ch 7
    cities = fr.read()

pat = re.findall(r'<ul>\s*(.*?)\s*</ul>', cities, re.M | re.DOTALL)

cities = pat[0]

my_cities = re.sub(r'<.*?>\s*(.*?)\s*<.*?>\s*<.*?>(.*?)<.*?>\s*<.*?>(.*?)<.*?>\s*<.*?>\s*<.*?>',
                   r'\1 - \2, \3', cities)

print(my_cities)
