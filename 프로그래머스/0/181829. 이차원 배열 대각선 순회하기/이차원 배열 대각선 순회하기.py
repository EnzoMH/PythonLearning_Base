def solution(board, k):
    total_sum = 0
    for i in range(len(board)):
        for j in range(len(board[i])):  # 열의 길이는 각 행의 길이로 접근해야 함
            if i + j <= k:
                total_sum += board[i][j]
    return total_sum