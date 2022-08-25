import sys

def div_ball(ball):
    global i
    if ball % 3 == 0:
        ball = ball % 3
        i += ball // 3
    elif ball % 2 == 0:
        ball = ball % 2
        i += ball // 2
    return ball
        
    
input = sys.stdin.readline
r, g, b = map(int, input().split())

i = 0
if div_ball(r)+div_ball(g)+div_ball(b) >= 1:
    i += 1
    
print(i)
