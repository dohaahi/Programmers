def solution(picture, k):
    answer = []
    
    for p in picture:
        new_str  = ''
        for s in list(p):
            new_str += s* k
        for i in range(k):
            answer.append(new_str)
    
    return answer