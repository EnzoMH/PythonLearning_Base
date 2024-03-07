def solution(arr):
    stk = []  # 스택 초기화
    i = 0  # 인덱스 초기화
    
    while i < len(arr):
        if not stk:  # stk가 빈 배열인 경우
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]:  # stk의 마지막 원소가 arr[i]보다 작은 경우
            stk.append(arr[i])
            i += 1
        else:  # stk의 마지막 원소가 arr[i]보다 크거나 같은 경우
            stk.pop()
    return stk