def solution(myString):
    result = ''.join(['l' if char < 'l' else char for char in myString])
    return result

# .transtable() 메서드 사용
def solution(myString):
    # 알파벳 'a'부터 'k'까지를 'l'로 매핑하는 변환 테이블 생성
    trans_table = str.maketrans('abcdefghijk', 'lllllllllll')
    # 변환 테이블을 사용하여 문자열 변환
    return myString.translate(trans_table)