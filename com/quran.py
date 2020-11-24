# with open('/home/nazmussaqib/Documents/Codes/JavaScript/com/sub/quran/allsurahs.txt', 'r') as fr:
#     surahs = fr.read()
#     surahs = surahs.split('\nبِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ')
#     for surah in surahs:
#         ser = surahs.index(surah) + 10
#         surah = surah.split('\n')
#         print(f'{ser}\t{surah}')
#         # with open(f'/home/nazmussaqib/Documents/Codes/JavaScript/com/sub/quran/surahsoriginal/{ser}.txt', 'a') as fw:
#         for ayah in surah:
#             print(f'{surah.index(ayah)}\t{ayah}')
#             # fw.write(f'{ayah}\n')
# import re
# with open('/home/nazmussaqib/Documents/Codes/JavaScript/com/sub/quran/bn.bengali.txt', 'r') as fr:
#     surahs = fr.read()
#     surahs = surahs.split('\n\n')
#     for surah in surahs:
#         ser = surahs.index(surah) + 1
#         surah = re.sub(r'\d{1,3}\|\d{1,3}\|', '', surah)
#         surah = surah.split('\n')
#         print(f'{ser}\t{surah}')
#         # with open(f'/home/nazmussaqib/Documents/Codes/JavaScript/com/sub/quran/surahsban/{ser}.txt', 'a') as fw:
#         for ayah in surah:
#             print(f'{surah.index(ayah)+1}\t{ayah}')
#             # fw.write(f'{ayah}\n')
# for i in range(1, 115):
#     with open(f'/home/nazmussaqib/Documents/Files/Quran/surahsoriginal/{i}.txt', 'r') as fror:
#         original = fror.read().split('\n')
#         with open(f'/home/nazmussaqib/Documents/Files/Quran/surahseng/{i}.txt', 'r') as freng:
#             eng = freng.read().split('\n')
#             with open(f'/home/nazmussaqib/Documents/Files/Quran/surahsban/{i}.txt', 'r') as frban:
#                 ban = frban.read().split('\n')
#                 json = '['
#                 for aya in range(1, len(original[1:-1])):
#                     ayah = original[aya].replace('"', r'\"')
#                     en = eng[aya - 1].replace('"', r'\"')
#                     bn = ban[aya - 1].replace('"', r'\"')
#                     json += f'''
#   {{
#     "num": "{aya}",
#     "ara": "{ayah}",
#     "eng": "{en}",
#     "ban": "{bn}"
#   }},'''
#                 orl = original[-2].replace('"', r'\"')
#                 enl = eng[-2].replace('"', r'\"')
#                 bnl = ban[-2].replace('"', r'\"')
#                 json += f'''
#   {{
#     "num": "{original.index(original[-2])}",
#     "ara": "{orl}",
#     "eng": "{enl}",
#     "ban": "{bnl}"
#   }}
# ]
# '''
#                 print(json)
#                 # with open(f'/home/nazmussaqib/Documents/Codes/JavaScript/com/sub/quran/surahs/{i}.json',
#                 #           'w') as jsonw:
#                 #     jsonw.write(json)
# # from os import mkdir
# qur = '''<!doctype html>
# <html>\n
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport"
#           content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
#     <meta http-equiv="X-UA-Compatible" content="ie=edge">
#     <title></title>
#     <link rel="shortcut icon" type="image/x-icon" href="../src/images/Quran-Logo.png"/>
#     <link rel="stylesheet" href="http://saqib.ml/src/styles.css">
#     <link rel="stylesheet" href="http://saqib.ml/src/dropdown.css">
#     <link rel="stylesheet" href="../src/styles.css">
#     <script src="http://saqib.ml/src/script.js"></script>
#     <script src="../src/surah.js"></script>
# </head>
#
# <body>
#     <header class="quran">
#         <h1 class="title">القرآن الكريم</h1>
#         <nav class="links">
#         <div class="dropdown">
#         <span>Menu</span>
#         <div id="burger"><span>&nbsp;</span><span>&nbsp;</span><span>&nbsp;</span><span>&nbsp;</span></div>
#         <ul>
#             <li><a href="http://saqib.ml/">Home</a></li>
#             <li class="dark"></li>
#             <li><a href="http://saqib.ml/about/">About</a></li>
#             <li><a href="../">Quran</a></li>
#             <li><a href="http://docs.saqib.ml/">Docs</a></li> <br/>
#         </ul>
#         </div>
#         </nav>
#
#         <h1 class="name"></h1>
#     </header>
#
#     <section class="surah"><figure><img src="../src/images/Spin.gif" alt="Loading"></figure></section>\n
#     <footer>
#         <span id="copy">Copyright <a href="/">Saqib</a> &copy; 2020 </span>
#         <ul>
#             <li><a href="mailto:nazmussaqib127@gmail.com" target="_blank"><span id="mail"></span></a></li>
#             <li><a href="https://facebook.com/m.nazmus.saqib/" target="_blank"><span id="facebook"></span></a></li>
#             <li><a href="https://wa.me/8801757055270" target="_blank"><span id="whatsapp"></span></a></li>
#             <li><a href="viber://chat?number=+8801757055270" target="_blank"><span id="viber"></span></a></li>
#         </ul>
#     </footer>
# </body>\n
# </html>
# '''
# for i in range(1, 115):
#     # mkdir(f'/home/nazmussaqib/Documents/Files/Quran/com/{i}')
#     with open(f'/home/nazmussaqib/Documents/Files/Quran/com/{i}/index.html', 'w') as f:
#         f.write(qur)
