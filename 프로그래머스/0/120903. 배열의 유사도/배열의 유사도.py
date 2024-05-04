def solution(s1, s2):
    s1_list = set(s1)
    s2_list = set(s2)    
    com_elem = s1_list.intersection(s2_list)
    return len(com_elem)