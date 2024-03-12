def solution(s):
    num = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    
    for n,ns in num.items():
        if ns in s:
            s = s.replace(ns,str(n))

    return int(s)