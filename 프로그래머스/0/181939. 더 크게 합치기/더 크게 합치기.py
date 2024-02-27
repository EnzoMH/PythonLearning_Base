def solution(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)

    if ab >= ba :
        return int(ab)
    else :
        return int(ba)