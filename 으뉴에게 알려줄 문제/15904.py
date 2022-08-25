import sys
input=sys.stdin.readline
s=list(input())
st=0
for i in "UCPC":
    try:
        st+=s[st:].index(i)
    except:
        st=0
        break
if st==0:
    print("I hate UCPC")
else:
    print("I love UCPC")
