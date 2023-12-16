def solution(myString):
    answer = ''

    for s in list(myString):
        answer += str.upper(s)
        
    return answer