def solution(hp):
    answer = hp // 5 + int(hp % 5 // 3) + int(hp % 5 % 3)
    return answer