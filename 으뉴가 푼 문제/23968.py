import sys

"""
앞에서 부터 탐색.
옆에 있는 두 수를 교환.

"""
def bubble_sort(arr, n , k):
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            if arr[j] > arr[j+1]:
                cnt += 1
                if cnt != k:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                else:
                    print(f"{arr[j]} {arr[j+1]}")
                    break
    if cnt < k:
        print(-1)           
    
input = sys.stdin.readline
n, k = map(int, input().rstrip().split()) # 배열 크기, 교환 횟수
arr = list(map(int, input().rstrip().split())) # 배열 입력 받기           
bubble_sort(arr, n, k) # 버블 정렬 실행
