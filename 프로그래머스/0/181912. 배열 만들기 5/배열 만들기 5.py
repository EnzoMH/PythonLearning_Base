def solution(intStrs, k, s, l):
    answer = []
    for numStr in intStrs:
        num = int(numStr[s:s+l])  # 시작 인덱스 s부터 길이 l만큼의 부분 문자열을 추출하여 정수로 변환
        if num > k:
            answer.append(num)
    return answer