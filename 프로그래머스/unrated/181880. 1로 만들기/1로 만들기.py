def solution(num_list):
    answer = 0

    for n in num_list:
        i = n
        while i > 1:
            answer += 1
            if i % 2 == 0:
                i = i / 2
                continue
            i = (i - 1) / 2

    return answer