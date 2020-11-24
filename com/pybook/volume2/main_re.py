import re  # Ch 7

countries = 'Afghanistan, America, Bangladesh, Canada, Denmark, ' \
            'England, Greenland, Iceland, Netherlands, New Zealand, Sweden, Switzerland'
land_countries = re.findall(r'(\w*lands*)', countries)
print(land_countries)


bangladesh = 'Bangladesh'
match = re.search(r'.', bangladesh)
print(match, '\n' + match.group())
match = re.search(r'B.n', bangladesh)
print(match, '\n' + match.group())
match = re.search(r'B.n...', bangladesh)
print(match, '\n' + match.group())

bangladesh = 'Bangladesh is our homeland'
match = re.search(r'B\w*h', bangladesh)
print(match, '\n' + match.group())
match = re.search(r'B.+?', bangladesh)
print(match, '\n' + match.group())


numbers = 'Multiple phone numbers: 01712833684, 017 57676289, 017 1115 1618, 00000000000, 123-123'
match = re.findall(r'01[3-9]\s*\d{4}\s*\d{4}', numbers)
print(match)

string = 'Bangla english bangla'
match = re.findall(r'^.*$', string, re.I)
print(match)


text = 'This is line 1. Date: 01/01/2020. There is another date: 06-07-2005. Another one: 19/05/2012'
pat = re.compile(r'(\d{2})[-/](\d{2})[-/](\d{4})')
print(pat)
result = pat.findall(text)
print(result)
text2 = '20/06/2015'
print(pat.findall(text2))

dates = '2005/07/06, 2012/05/19, 2020/01/01'
new_dates = re.sub(r'(\d{4})/(\d{2})/(\d{2})', r'\3-\2-\1', dates)
print(new_dates)


message = 'Email: nazmussaqib@gmail.com, nazmus@saqib, nazmul@gmail.com'
emails = re.findall(r'([.\w]+@\w+[.]\w+)', message)
print(emails)
message = 'saqib at gmail.com, saqib (at) gmail.com, saqib [at] gmail.com, saqib At gmail.com'
emails = re.sub(r'\s+[(\[]*\s*at\s*[)\]]*\s+', '@', message, flags=re.I)
print(emails)
message = 'saqib@gmail dot com, saqib@gmail Dot com, saqib@gmail [dot] com, saqib@gmail (dot) com'
emails = re.sub(r'\s+[(\[]*\s*dot\s*[)\]]*\s+', '.', message, flags=re.I)
print(emails)

emails = 'saqib at gmail dot com, saadat At gmail (dot) com, seaum [at] gmail Dot com, kafi (at) gmail [dot] com'
print(emails)
emails = re.sub(r'\s+[(\[]*\s*at\s*[)\]]*\s+', '@', emails, flags=re.I)
print(emails)
emails = re.sub(r'\s+[(\[]*\s*dot\s*[)\]]*\s+', '.', emails, flags=re.I)
print(emails)
