def solution(my_string):
    numbers = []
    for char in my_string:
        if char.isdigit():  # 문자가 숫자인지 확인
            numbers.append(int(char))  # 숫자면 숫자 리스트에 추가
    return sorted(numbers)  # 숫자 리스트를 오름차순으로 정렬하여 반환
