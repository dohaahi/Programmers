def solution(dots):
    a, b, c, d = dots

    set_a = {a[0], b[0], c[0], d[0]}
    set_b = {a[1], b[1], c[1], d[1]}
    
    len_a = abs(list(set_a)[0] - list(set_a)[1])
    len_b = abs(list(set_b)[0] - list(set_b)[1])

    return len_a * len_b