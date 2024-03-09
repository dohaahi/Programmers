def solution(s):
    p = 0
    y = 0

    for a in str.lower(s):
        if a == 'p':
            p += 1
        elif a == 'y':
            y += 1

    if p == y:
        return True
    else:
        return False