def solution(str):
    answer = []
    s_list = list(str)

    for n in range(len(s_list)):
        if s_list[:n].count(s_list[n]) == 0:
            answer.append(-1)
        else:
            index = s_list.index(s_list[n])
            s_list[index] = " "
            answer.append(n - index)

    return answer