import sys

def insertion_sort(arr, n, k):
    cnt = 0
    for i in range(1, n): # 두번째 요소부터 시작
        key = arr[i] # key로 요소 저장
        for j in reversed(range(i)): # i-1 ~ 0 까지 역순으로 탐색 
            if key < arr[j]: # key가 더 작은 수인 경우
                cnt += 1 # 카운트 1 증가
                if cnt == k: # 카운트와 k가 같으면
                    print(arr[j]) # 출력
                arr[j+1] = arr[j] # 오른쪽 요소를 왼쪽 요소로 저장
                if j == 0: # key가 0번째 요소가 되는 경우
                    cnt += 1 # 카운트 1 증가
                    if cnt == k: # 카운트와 k가 같으면
                        print(key) # 출력
                    arr[0] = key 
                
            else: # key가 큰 수인 경우
                if arr[j+1] != key: # key와 요소가 다른 수인 경우 
                    cnt += 1 # 카운트 1 증가
                    if cnt == k: 
                        print(key)
                arr[j+1] = key 
                break
                
    if cnt < k:
        print(-1)         

input = sys.stdin.readline
n, k = map(int, input().rstrip().split()) # 배열 크기, 교환 횟수
arr = list(map(int, input().rstrip().split())) # 배열 입력 받기    
insertion_sort(arr, n, k)


