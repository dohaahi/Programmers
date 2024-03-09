def solution(a, b):
    if a < b:
        return sum(a for a in range(a,b+1))
    else:
        return sum(a for a in range(b,a+1))  