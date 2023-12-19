def solution(myString):
    answer = ''
    
    for s in myString:
        if ord(s) < ord('l'):
            answer += 'l'
            continue
        answer += s

    return answer