import sys,math
input=sys.stdin.readline
s,t,f,f2=0,0,0,0

#입력 받고 f, f2, t 변수에 카운트
for _ in range(int(input())):
    a=input().rstrip()
    if a=="1/4":
        f+=1
    elif a=="3/4":
        f2+=1
    elif a=="1/2":
        t+=1
s+=t//2 # 1/2 개수를 2로 나눈 몫을 s에 저장
t %= 2 # 나머지를 t에 저장

if f2>f: 
    s+=f
    f2-=f
    s+=f2
    s+=t
else:
    s+=f2
    f-=f2
    s+=t*0.5+f*0.25
print(math.ceil(s))
