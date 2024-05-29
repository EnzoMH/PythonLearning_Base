def solution(chicken):
    answer = 0
    while chicken >= 10:
        div = chicken // 10
        mod = chicken % 10
        answer += div
        chicken = div+mod
    return answer

# 치킨 1마리당 쿠폰 한장이 발급된다
# 치킨 10마리를 시켜먹으면 1마리가 공짜다
# 공짜인 1마리도 서비스쿠폰이 발급된다
# 치킨 갯수가 정해졌을 때 최대 서비스 치킨의 수는 얼마인가