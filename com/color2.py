# main code: https://gist.github.com/dylnmc/93e9d0e923adccc73487431066125853
# sample .png: https://i.stack.imgur.com/OK3po.png
# my code (python): https://pastebin.com/u6ux6ca6
# my code (java): https://pastebin.com/tydc9jet

e = chr(27) + '['

for n in range(0, 8):
    print('%s38;05;%dm\t(%d)' % (e, n, n), end=' ')
print('%s0m' % e)

for n in range(8, 16):
    print('%s38;05;%dm\t(%d)' % (e, n, n), end=' ')
print('%s0m' % e, '\n')

step = 6
start = 16

for i in range(0, 6):
    for j in range(0, 12):
        if j < 6:
            n = (start + (j * step) + i)
        else:
            n = (start + ((17 - j) * step) + i)
        print('%s38;05;%dm\t(%d)' % (e, n, n), end=' ')
    print('%s0m' % e)
print()

start = 93
for i in range(0, 6):
    for j in range(0, 12):
        if j < 6:
            n = (start + (j * step) - i)
        else:
            n = (start + ((17 - j) * step) - i)
        print('%s38;05;%dm\t(%d)' % (e, n, n), end=' ')
    print('%s0m' % e)
print()

start = 160
for i in range(0, 6):
    for j in range(0, 12):
        if j < 6:
            n = (start + (j * step) + i)
        else:
            n = (start + ((17 - j) * step) + i)
        print('%s38;05;%dm\t(%d)' % (e, n, n), end=' ')
    print('%s0m' % e)
print()
for n in range(232, 244):
    print('%s38;05;%dm\t(%d)' % (e, n, n), end=' ')
print('%s0m' % e)

for n in range(244, 256):
    print('%s38;05;%dm\t(%d)' % (e, n, n), end=' ')
print('%s0m' % e)
