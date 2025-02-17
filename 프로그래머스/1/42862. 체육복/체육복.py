def solution(n, lost, reserve):
    answer = n - len(lost)

    lost.sort()
    reserve.sort()

    for l in lost.copy():
        if l in reserve:
            reserve.remove(l)
            lost.remove(l)
            answer += 1

    for l in lost:
        if l - 1 in reserve:
            answer += 1
            reserve.remove(l - 1)
        elif l + 1 in reserve:
            answer += 1
            reserve.remove(l + 1)

    return answer