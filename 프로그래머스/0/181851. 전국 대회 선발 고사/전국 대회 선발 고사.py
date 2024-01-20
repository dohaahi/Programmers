def solution(rank, attendance):
    result = []

    for r, a in zip(rank, attendance):
        if a:
            result.append(r)

    result.sort(reverse=False)

    return 10000 * rank.index(result[0]) + 100 * rank.index(result[1]) + rank.index(result[2])