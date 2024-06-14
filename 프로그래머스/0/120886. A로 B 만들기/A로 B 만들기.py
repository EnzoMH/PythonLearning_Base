#def solution(before, after):
#    b_list = list(before)
#    a_list = list(after)
#    if b_list.reverse() == a_list :
#        return 1
 #   else :
 #       return 0
    
def solution(before, after):
# before와 after를 각각 정렬
    sorted_before = sorted(before)
    sorted_after = sorted(after)
    # 정렬된 두 리스트를 비교
    if sorted_before == sorted_after:
        return 1
    else:
        return 0
#1.before, after 배열로 바꾼 후
#2. if문
#3. after의 swapcase 가 before일시 1 return, else, 0 return