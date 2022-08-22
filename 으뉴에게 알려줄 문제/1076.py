import sys
input=sys.stdin.readline
a=["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
s=0
s+=a.index(input().rstrip())*10
s+=a.index(input().rstrip())
for _ in range(a.index(input().rstrip())):
    s*=10
print(s)
