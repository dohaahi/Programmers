def solution(str):
    answer = ''

    i = 0
    for s in str.lower():
        if s == ' ':
            i = 0
            answer += ' '

        else:
            if i % 2 == 0:
                answer += s.upper()
            else:
                answer += s
            i += 1

    return answer