import sys

"""
앞에서 부터 탐색.
옆에 있는 두 수를 교환.
점점 범위가 줄어든다.
"""
def bubble_sort(arr, n , k):
    cnt = 0
    for i in range(n-1, -1, -1): # n-1부터 0까지 1씩 줄어든다
        for j in range(0, i): # 0부터 i까지 참색
            if arr[j] > arr[j+1]: # 왼쪽 수가 더 큰 경우
                cnt += 1 # 카운트 1 증가
                if cnt != k: # 카운트가 k에 도달하지 않은 경우
                    arr[j], arr[j+1] = arr[j+1], arr[j] # 교환
                else:
                    print(f"{arr[j+1]} {arr[j]}") # 출력
                    break
    if cnt < k:
        print(-1)           
    
input = sys.stdin.readline
n, k = map(int, input().rstrip().split()) # 배열 크기, 교환 횟수
arr = list(map(int, input().rstrip().split())) # 배열 입력 받기           
bubble_sort(arr, n, k)      
