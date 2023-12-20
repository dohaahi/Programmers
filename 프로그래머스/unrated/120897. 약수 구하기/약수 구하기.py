def solution(n):
    answer = []
    
    for num in range(n):
        if n % (num + 1) == 0:
            answer.append(num+1)
    
    return answer