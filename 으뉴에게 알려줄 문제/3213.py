import sys,math
input=sys.stdin.readline
s,t,f,f2=0,0,0,0
for _ in range(int(input())):
    a=input().rstrip()
    if a=="1/4":
        f+=1
    elif a=="3/4":
        f2+=1
    elif a=="1/2":
        t+=1
s+=t//2
t%=2
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
