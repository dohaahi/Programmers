def solution(lottos, win_nums):
    answer = [0, 0]

    count, zero = 0, 0

    for n in lottos:
        if n in win_nums:
            count += 1
        if n == 0:
            zero += 1
            
    if zero == 6:
        return [1,6]

    answer[0] = 7 - count - zero if count != 0 else 6
    answer[1] = 7 - count if count != 0 else 6

    return answer