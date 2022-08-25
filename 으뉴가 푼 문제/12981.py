import sys        
    
input = sys.stdin.readline
r, g, b = map(int, input().split())

box = 0
mod_is_0 = 0

if r % 3 == 0:
    mod_is_0 += 1
box += r // 3
r %= 3

if g % 3 == 0:
    mod_is_0 += 1
box += g // 3
g %= 3

if b % 3 == 0:
    mod_is_0 += 1
box += b // 3
b %= 3

if mod_is_0 == 2:
    print(box+1)
else:
    print(box+max(r,g,b))
