def solution(my_str, n):
    answer = []

    for i in range(len(my_str)//n+1):
        new_str = my_str[i * n:(i + 1) * n]
        if new_str == '':
            continue
        answer.append(new_str)
    return answer