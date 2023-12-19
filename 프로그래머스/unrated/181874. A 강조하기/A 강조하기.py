def solution(myString):
    answer = ''
    
    for s in myString:
        if s == 'a' or s == 'A':
            answer += s.upper()
            continue
        answer+= s.lower()
        
    return answer