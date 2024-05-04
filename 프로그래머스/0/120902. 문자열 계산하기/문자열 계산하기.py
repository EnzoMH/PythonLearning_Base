# def solution(my_string):
#     answer = 0
#     cal_list = list(my_string)
#     if cal_list[1] == "+" :
#         return cal_list[0] + cal_list[2]
#     elif cal_list[1] == "-" :
#         return cal_list[0] - cal_list[2]
#     else :
#         return cal_list

# def solution(my_string):    
#     cal_list = my_string.split() # 공백을 기준으로 수식을 분리    
#     answer = int(cal_list[0]) # 첫 번째 숫자를 결과값으로 초기화
#     for i in range(1, len(cal_list), 2): # 두 번째 숫자부터 연산자와 함께 반복하여 계산합니다.
#         operator = cal_list[i]
#         num = int(cal_list[i + 1])
#         if operator == "+": # 덧셈인 경우
#             answer += num
#         elif operator == "-": # 뺄셈인 경우
#             answer -= num
#     return answer

solution = eval
