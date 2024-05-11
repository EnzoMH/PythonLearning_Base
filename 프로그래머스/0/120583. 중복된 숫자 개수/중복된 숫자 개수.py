# 슈도코드 기반 작성
# def solution(array, n):
#     answer = 0
#     n_array = []
#     for i in array :
#         if n in array :
#             # n_array.append # 현재 작성하지 못한코드
#     return len(n_array)

def solution(array, n):
    count = 0
    for i in array:
        if i == n:
            count += 1
    return count

# 더 간결한 코드
def solution(array, n):
    return array.count(n)