def solution(common):
    if len(common) < 2:
        return None  # 수열의 길이가 2 미만이면 처리 불가
    if common[1] - common[0] == common[2] - common[1]:
        difference = common[1] - common[0]
        return common[-1] + difference
    elif common[1] / common[0] == common[2] / common[1]:
        ratio = common[1] / common[0]
        return common[-1] * ratio
    else:
        return None  # 등차수열도 등비수열도 아닌 경우 처리 불가