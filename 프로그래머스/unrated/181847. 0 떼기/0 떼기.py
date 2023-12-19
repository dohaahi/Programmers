def solution(n_str):
    answer = ''
     
    for s in n_str:
        if s == '0' and len(answer) == 0:
            continue
        answer+= s
    
    return answer