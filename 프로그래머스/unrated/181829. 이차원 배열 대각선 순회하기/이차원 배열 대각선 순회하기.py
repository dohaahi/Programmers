def solution(board, k):
    answer = 0
    
    for i in range(len(board)):
        for s in range(len(board[i])):
            if i + s <= k: 
                answer += board[i][s]
    
    return answer