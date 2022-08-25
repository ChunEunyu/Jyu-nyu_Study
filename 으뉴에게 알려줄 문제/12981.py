"""
우선 필요한 박스의 개수가 최솟값이 되려면 한 상자에 3개를 담는 경우가 많아야 돼
만약 어떤 색의 공이 3개 이상 있다면 그 공 3개를 한 박스에 넣음으로써 상자가 꽉 차게 넣어줄 수 있쥐
ex) RRGGGBBBBB > RR (GGG) (BBB) BB
이렇게 묶어두고 남은 공들은 서로 색이 다르게 박스에 넣어주면 끝!
ex) RR (GGG) (BBB) BB > (GGG) (BBB) (RB) (RB)
이 예시가 사이트 예제 4번과 같오

그런데 주의해야할 부분 한가지
만약 RR 이런 경우에 이 방법대로 하면 (R)(R) 이렇게 2개로 묶여버려
이거만 따로 if문으로 구별해주면 완성!!
"""
import sys
input=sys.stdin.readline
R,G,B=map(int,input().split())
s=0
z=0
if R%3==0:
    z+=1
s+=R//3
R%=3
if G%3==0:
    z+=1
s+=G//3
G%=3
if B%3==0:
    z+=1
s+=B//3
B%=3
if z==2:
    print(s+1)
else:
    print(s+max(R,G,B))
