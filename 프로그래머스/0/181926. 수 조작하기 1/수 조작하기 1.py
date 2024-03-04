def solution(n, control):
    for char in control:
        if char == "w":
            n += 1
        elif char == "s":
            n -= 1
        elif char == "d":
            n += 10
        elif char == "a":
            n -= 10
    return n

# 예시 호출
n = 0
control = "wsdawsdassw"
print(solution(n, control))
