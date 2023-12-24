def solution(before, after):
    a, b = sorted(before), sorted(after)
    return int(a == b)