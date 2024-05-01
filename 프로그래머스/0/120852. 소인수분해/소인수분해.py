# def solution(n):
#     answer = []
#     for num in range(2, n + 1):
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             answer.append(num)
#     return sorted(answer)
def solution(n):
    answer = []
    divisor = 2  # 가장 작은 소수인 2부터 시작합니다.    
    while n > 1:  # n이 1보다 큰 동안에만 소인수분해를 반복합니다.
        if n % divisor == 0:  # 현재 divisor로 나누어떨어지면 소인수입니다.
            answer.append(divisor)  # 소인수를 추가합니다.
            n //= divisor  # n을 divisor로 나눈 몫으로 업데이트합니다.
        else:
            divisor += 1  # 나누어떨어지지 않으면 다음 소수를 시도합니다.    
    return sorted(list(set(answer)))  # 중복 제거 후 정렬된 소인수 리스트를 반환합니다.


