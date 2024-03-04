def solution(a, d, included):
    sum = 0  # 합계를 저장할 변수 초기화
    for i in range(len(included)):  # included 리스트의 길이만큼 반복
        if included[i]:  # 해당 항이 True인 경우
            sum += a + d * i  # 등차수열의 해당 항을 합계에 더함
    return sum  # 계산된 합계 반환