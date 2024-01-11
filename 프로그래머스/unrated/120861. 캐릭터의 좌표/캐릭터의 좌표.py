def solution(keyinput, board):
    answer = [0, 0]

    for m in keyinput:
        if m == 'up' or m == 'down':
            new_position = answer[1]
            if m == 'up':
                new_position = answer[1] + 1
            elif m == 'down':
                new_position = answer[1] - 1

            if new_position < -(board[1]//2) or new_position > board[1]//2:
                continue
            answer[1] = new_position

        else:
            new_position = answer[0]
            if m == 'left':
                new_position = answer[0] - 1
            elif m == 'right':
                new_position = answer[0] + 1

            if new_position < -(board[0]//2) or new_position > board[0]//2:
                continue
            answer[0] = new_position

    return answer