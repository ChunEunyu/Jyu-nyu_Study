import sys

input=sys.stdin.readline
s=list(input()) # 리스트로 입력 받기
st=0

for i in "UCPC":
    try: # s 리스트에 i 문자가 있는 인덱스 위치를 st 변수에 저장
        st+=s[st:].index(i) 
    except:
        st=0
        break
if st==0: # ucpc가 s 리스트에 없는 경우
    print("I hate UCPC")
else:
    print("I love UCPC")
