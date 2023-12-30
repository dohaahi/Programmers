def solution(arr):
    answer = 0
    be_arr= arr
    next_arr= []
    
    while be_arr != next_arr:
        if answer != 0:
            be_arr=next_arr
        next_arr = ss(be_arr)
        answer+=1

    return answer-1

def ss(arr):
    next_arr=[]
    for n in arr:
        if n >= 50 and n % 2 == 0:
            n //= 2
        elif n < 50 and n % 2 != 0:
            n = n * 2 + 1
        next_arr.append(n)
    return next_arr