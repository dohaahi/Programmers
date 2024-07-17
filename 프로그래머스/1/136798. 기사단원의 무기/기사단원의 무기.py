def solution(number, limit, power):
    answer = 1
    
    for n in range(2, number + 1):
        divisor = 2
        for i in range(2,int(n ** 0.5) + 1):
            if i ** 2 == n:
                divisor +=1
            elif n % i == 0:
                divisor += 2
        if divisor > limit:
            answer += power
        else:
            answer += divisor
            
    return answer