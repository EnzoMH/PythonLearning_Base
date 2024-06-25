def solution(s):
    s = s.lower()  # 문자열을 모두 소문자로 변환하여 대소문자 구분 없이 비교할 수 있도록 함
    count_p = s.count('p')  # 'p'의 개수 세기
    count_y = s.count('y')  # 'y'의 개수 세기
   
    return count_p == count_y  # 'p'와 'y'의 개수가 같으면 True, 다르면 False 반환