def solution(sides):
    a, b = sorted(sides)  # Ensure a <= b
    min_c = b - a + 1     # 최소 길이
    max_c = a + b - 1     # 최대 길이
    return max_c - min_c + 1
