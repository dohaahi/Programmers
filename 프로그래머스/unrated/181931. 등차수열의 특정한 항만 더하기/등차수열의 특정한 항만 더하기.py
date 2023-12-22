def solution(a, d, included):
    return sum(int(a) + int(d) * i for i in range(len(included)) if included[i])