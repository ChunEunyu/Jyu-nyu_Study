import sys

input = sys.stdin.readline
colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white'] 

s = 0
s += colors.index(input().rstrip())*10 # 해당 인덱스에 10을 곱하여 s 변수에 저장
s += colors.index(input().rstrip()) # 해당 인덱스를 s 변수에 저장
for _ in range(colors.index(input().rstrip())): # 인덱스 수 만큼 s에 10을 곱해준다.
    s *= 10

print(s)

'''
입력: 
yellow
violet
red

과정:
s = 40
s = 47
s = 47 * 10 * 10 = 4700

출력:
4700
'''
