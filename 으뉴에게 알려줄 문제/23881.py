import sys
input = sys.stdin.readline

def selection_sort(A, N, K): # 선택 정렬 함수
    c = 0 # 정렬 횟수 카운트
    for i in reversed(range(1, N)): # i가 N-1부터 1까지 1씩 감소
        if A[i] < max(A[0:i]):
            c+=1 # 정렬 횟수 증가
            if c != K: # 교환 횟수가 K에 도달하지 못한 경우
                ind = A.index(max(A[0:i])) # 그냥 선택 정렬 방법대로 정렬
                t = A[ind]
                A[ind] = A[i]
                A[i] = t
            else: # 교환 횟수가 K에 도달한 경우
                print(str(A[i]) + " " + str(max(A[0:i]))) # 교환되는 수 출력
                break
    if c < K: # for문이 끝난(즉, 정렬이 끝난) 경우에 여전히 교환 횟수가 K에 도달하지 못한 경우
        print(-1)

n, k = map(int, input().split()) # 배열 크기 N, 교환 횟수 K
a = []
a = list(map(int, input().split())) # 배열 입력
selection_sort(a, n, k)
