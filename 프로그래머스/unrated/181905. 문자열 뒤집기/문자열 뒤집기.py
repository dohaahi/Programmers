def solution(my_string, s, e):
    answer = my_string[:s]

    ss = my_string[s:e + 1]
    answer += ss[::-1]
    answer += my_string[e+1:]

    return answer