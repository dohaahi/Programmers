def solution(numLog):
    answer = ''
    
    for i in range(len(numLog)-1):
        s = numLog[i] - numLog[i+1]
        if s == 1:
            answer += 's'
        elif s == -1:
            answer+='w'
        elif s == 10:
            answer+='a'
        else:
            answer+='d'
        
    return answer