def solution(picture, k):
    expanded_picture = []
    
    for row in picture:
        expanded_row = ''
        for pixel in row:
            expanded_row += pixel * k
        for _ in range(k):
            expanded_picture.append(expanded_row)
    
    return expanded_picture