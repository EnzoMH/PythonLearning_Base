def solution(num, total):
    middle = total // num
    start = middle - (num // 2) + (1 if num % 2 == 0 else 0)
    return [start + i for i in range(num)]
    
#1. 중간값
#2. 짝수 / 홀수 