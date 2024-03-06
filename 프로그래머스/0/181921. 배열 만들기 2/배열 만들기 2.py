def solution(l, r):
    arr = []  # 결과를 저장할 리스트 초기화
    for i in range(l, r+1):  # l부터 r까지 순회
        num_str = str(i)  # 현재 숫자를 문자열로 변환
        digits = set(num_str)  # 문자열의 각 문자를 유니크한 요소로 가지는 집합 생성
        # 조건 검사: 숫자가 "0"과 "5"만 포함하는지 확인
        if digits.issubset({"0", "5"}):
            arr.append(i)  # 조건을 만족하면 리스트에 추가
    if not arr:  # 조건을 만족하는 숫자가 없다면
        arr.append(-1)  # [-1] 반환
    return arr
