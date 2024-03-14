def solution(answers):
    answer = []

    p1 = [1, 2, 3, 4, 5][:len(answers)] if len(answers) < 5 else ([1, 2, 3, 4, 5] * ((len(answers) // 5) + 1))[
                                                                 :len(answers)]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5][:len(answers)] if len(answers) <= 8 else ([2, 1, 2, 3, 2, 4, 2, 5] * ((
                                                                                                                len(answers) // 8) + 1))[
                                                                           : len(answers)]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][:len(answers)] if len(answers) <= 10 else ([3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * ((
                                                                                                                             len(answers) // 10) + 1))[
                                                                                  :len(answers)]

    count = [0, 0, 0]

    for z, x, c, a in zip(p1, p2, p3, answers):
        if z == a:
            count[0] += 1
        if x == a:
            count[1] += 1
        if c == a:
            count[2] += 1

    for i in range(len(count)):
        max_num = max(count)

        if max_num == 0:
            return []
        if count[i] == max_num: \
                answer.append(i + 1)

    return answer