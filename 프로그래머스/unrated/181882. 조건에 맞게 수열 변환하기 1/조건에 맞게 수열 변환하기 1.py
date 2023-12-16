def solution(arr):
    answer = []

    for i in arr:
        if i < 50 and i % 2 != 0:
            answer.append(i * 2)
            continue
            
        elif i >= 50 and i % 2 == 0:
            answer.append(i / 2)
            continue
        
        else:
            answer.append(i)

    return answer