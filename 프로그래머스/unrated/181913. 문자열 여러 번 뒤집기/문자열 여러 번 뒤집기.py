def solution(my_string, queries):
    answer = my_string[:]

    for n, m in queries:
        new_str = ''
        new_str += answer[:n]
        new_str += answer[n:m + 1][::-1]
        new_str += answer[m + 1:]
        answer = new_str[:]

    return answer