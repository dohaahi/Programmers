def solution(sides):
    sides.sort()
    answer = sides[0] - 1

    for i in range(sides[1]+1):
        if sides[0] + i > sides[1]:
            answer += 1

    return answer