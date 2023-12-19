def solution(myString, pat):
    answer = ''

    for s in myString:
        if s == "A":
            answer += "B"
            continue
        answer += "A"
    
    return int(pat in answer)