import sys

input = sys.stdin.readline
string = input()
ucpc = ['U','C','P','C']

for s in string:
    if ucpc: # ucpc 리스트가 비어있지 않음
        if s == ucpc[0]: # s 문자와 ucpc 첫번째 문자가 같으면
            del ucpc[0] # ucpc 첫번째 요소 삭제

print('I love UCPC' if not ucpc else 'I hate UCPC') # ucpc 리스트에 아무것도 없으면 성공
