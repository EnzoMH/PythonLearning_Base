# 슈도코드 기반 작성
# def solution(my_str, n):
#     answer = []
#     new_list = list(my_str)
#     i for i in answer(:int(new_list[n-1]):int(new_list[n])) :
#     return answer

def solution(my_str, n):
    answer = []
    # 문자열을 n 길이로 자르고 배열에 저장하는 과정
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n])
    return answer

# 더 간결한 코드
def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]