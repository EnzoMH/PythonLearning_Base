def solution(n):
    answer = 0
    number = str(n)  # 정수 N을 문자열로 변환하여 각 자릿수에 접근하기 쉽게 함
    
    for index in number:
        answer += int(index)  # 각 자릿수를 정수로 변환하여 sum_of_digits에 더함
    
    return answer