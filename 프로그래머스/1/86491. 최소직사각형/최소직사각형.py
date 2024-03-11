def solution(sizes):
    d = []
    h = []
    
    for l in sizes:
        l.sort()
        d.append(l[0])
        h.append(l[1])
    
    return max(d)*max(h)