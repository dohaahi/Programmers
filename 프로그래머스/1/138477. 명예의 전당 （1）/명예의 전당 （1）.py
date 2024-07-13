def solution(k, score):

    answer = []
    best = []

    for i in score:
        if len(best) < k:
            best.append(i)
            answer.append(min(best))
        else:
            if i > min(best):
                best.remove(min(best))
                best.append(i)
            answer.append(min(best))
    return answer