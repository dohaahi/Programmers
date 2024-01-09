def solution(arr, k):
    answer = []
    
    for n in arr:
        if len(answer) == k:
            return answer
        
        if n not in answer:
            answer.append(n)
    
    if len(answer) < k:
        while len(answer) < k:
            answer.append(-1)
    
    return answer