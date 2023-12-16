import math

def solution(n):
    if n % 2 == 0:
        return sum(math.pow(i,2) for i in range(0,n+1,2))
    
    return sum(i for i in range(1, n+1, 2))