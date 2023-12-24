def solution(intStrs, k, s, l):
    answer = []

    for n in intStrs:
        answer.append(n[s:s+l])

    return [int(nn) for nn in answer if int(nn) > k]
