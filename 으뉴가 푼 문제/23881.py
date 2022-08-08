import sys

def selection(arr, n, k):
    cnt = 0 # 카운트
    for i in range(n-1, 0, -1): # 역순으로 1씩 감소하면서 탐색
        if arr[i] < max(arr[0:i]): # arr[0 ~ i-1]내 가장 큰 값이 arr[i] 값보다 큰 경우
            cnt += 1 # 카운트 1 증가
            if cnt != k: # 아직 카운트값이 k값에 도달하지 않은 경우
                idx = arr.index(max(arr[0:i])) # 맥스값의 인덱스를 idx 변수에 저장
                target = arr[idx] # target 변수에 기존 idx 인덱스 값 저장
                arr[idx], arr[i] = arr[i], target # idx와 i 인덱스 값을 교환, target 변수에 교환된 값을 저장
            else: # 카운트 값과 k가 같은 경우
                print(f"{arr[i]} {max(arr[0:i])}") # 교환된 인덱스의 값을 출력
                break
    if cnt < k: 
        print(-1)
            
input = sys.stdin.readline
n, k = map(int, input().rstrip().split()) # 배열 크기, 교환 횟수
arr = list(map(int, input().rstrip().split())) # 배열 입력 받기           
selection(arr, n, k)      
