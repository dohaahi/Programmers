def solution(a, b):
    ss = str(a) + str(b)
    tt = 2 * a * b
    
    if tt > int(ss):
        return tt
    
    return int(ss)