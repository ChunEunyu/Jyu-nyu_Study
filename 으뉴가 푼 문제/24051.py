import sys

def insertion_sort(arr, n, k):
    cnt = 0
    for i in range(n):
        key = arr[i] 
        for j in range(i, 0, -1): 
            if key < arr[j-1]:
                cnt += 1
                if cnt != k:
                    arr[j-1], arr[j] = arr[j], arr[j-1]
                else:
                    print(f"{arr[j]}")
                    break
    if cnt < k:
        print(-1)         

input = sys.stdin.readline
n, k = map(int, input().rstrip().split()) # 배열 크기, 교환 횟수
arr = list(map(int, input().rstrip().split())) # 배열 입력 받기    
insertion_sort(arr, n, k)
