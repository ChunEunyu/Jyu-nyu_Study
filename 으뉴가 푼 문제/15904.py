import sys

input = sys.stdin.readline
str1 = input().rstrip()
res = ''

for s in str1:
    if 65 <= ord(s) < 97:
        res += s

if res == 'UCPC':
    print('I love UCPC')
else:
    print('I hate UCPC')
