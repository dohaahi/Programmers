import math 

def solution(a, b):
    if a % 2 != 0 and b % 2 != 0:
        return math.pow(a, 2) + math.pow(b, 2)
    elif a % 2 == 0 and b % 2 == 0:
        return abs(a - b)
    else:
        return 2 * (a + b)