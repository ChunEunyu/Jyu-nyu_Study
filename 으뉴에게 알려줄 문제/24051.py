import sys
input = sys.stdin.readline

def insertion_sort(A, N, K):
    c = 0
    for i in range(1, N):
        m = A[i]
        l = i-1
        while(l >= 0):
            if A[l] > m:
                c+=1
                if c == K:
                    print(A[l])
                A[l+1] = A[l]
                l -= 1
            else:
                if A[l+1] != m:
                    c+=1
                    if c == K:
                        print(m)
                    A[l+1] = m
                break
        if l < 0:
            c+=1
            if c == K:
                print(m)
            A[0]=m
    if c < K:
        print(-1)

N, K = map(int, input().split())
A = list(map(int, input().split()))
insertion_sort(A, N, K)
