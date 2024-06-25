def solution(arr):
    num_rows = len(arr)
    num_cols = len(arr[0]) if arr else 0

    if num_rows > num_cols:
        for row in arr:
            row.extend([0] * (num_rows - num_cols))
    elif num_cols > num_rows:
        for _ in range(num_cols - num_rows):
            arr.append([0] * num_cols)
    
    return arr