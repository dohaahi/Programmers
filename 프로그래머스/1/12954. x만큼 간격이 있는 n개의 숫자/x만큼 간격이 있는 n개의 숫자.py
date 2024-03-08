def solution(x, n):
    if x == 0:
        return [0]*n
    
    if x < 0:    
        return [-a for a in range(-x , -x *n+1,-x)]
        
    return [a for a in range(x, x*n+1,x)]