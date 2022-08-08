import sys

def insertion_sort(arr, n, k):
    cnt = 0
    for i in range(1, n):
        key = arr[i]
        for j in reversed(range(i)):
            if key < arr[j]:
                cnt+=1
                if cnt == k:
                    print(arr[j])
                arr[j+1] = arr[j]
                if j == 0:
                    cnt+=1
                    if cnt == k:
                        print(key)
                    arr[0]=key
            else:
                if arr[j+1] != key:
                    cnt+=1
                    if cnt == k:
                        print(key)
                arr[j+1]=key
                break
    if cnt < k:
        print(-1)         

input = sys.stdin.readline
n, k = map(int, input().split()) # 배열 크기, 교환 횟수
arr = list(map(int, input().split())) # 배열 입력 받기    
insertion_sort(arr, n, k)
