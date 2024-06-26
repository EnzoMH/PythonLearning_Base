# def solution(arr, delete_list):
#     combined = list(zip(arr, delete_list))
#     comtuple = [tuple(pair) for pair in combined]
#     return comtuple - delete_list

def solution(arr, delete_list):
    # delete_list에 포함되지 않은 원소들로 이루어진 새로운 배열 생성
    result = [elem for elem in arr if elem not in delete_list]
    return result