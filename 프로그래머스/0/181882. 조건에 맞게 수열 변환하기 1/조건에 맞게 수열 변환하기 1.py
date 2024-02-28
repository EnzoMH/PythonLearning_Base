def solution(arr):
    # 결과를 저장할 새로운 배열을 초기화합니다.
    result = []
    
    # arr 배열의 각 원소에 대해 반복합니다.
    for num in arr:
        # 조건에 따라 적절한 연산을 수행합니다.
        if num >= 50 and num % 2 == 0:
            # 값이 50보다 크거나 같은 짝수라면 2로 나눕니다.
            result.append(num // 2)
        elif num < 50 and num % 2 != 0:
            # 값이 50보다 작은 홀수라면 2를 곱합니다.
            result.append(num * 2)
        else:
            # 그 외의 경우 원소를 그대로 결과 배열에 추가합니다.
            result.append(num)
    
    # 변형된 배열을 반환합니다.
    return result