def solution(number):
    n_str = str(number)  # 자연수를 문자열로 변환
    n_list = list(n_str)  # 문자열을 각 문자(character)를 요소로 가지는 리스트로 변환
    n_list.reverse()  # 리스트를 뒤집음
    
    # 각 요소를 정수로 변환하여 반환
    return [int(x) for x in n_list]