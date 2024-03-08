def solution(n):
    answer = 0

    for s in list(str(n)):
        answer += int(s)

    return answer