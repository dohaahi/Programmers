def solution(score):
    answer = [1] * len(score)

    avg_list = list(map(lambda s: sum(s), score))

    num = 0
    for i in range(len(score)):
        num = avg_list[i]
        for j in range(len(avg_list)):
            if avg_list[j] < num:
                answer[j] += 1

    return answer