from collections import Counter

def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)

    result = (p - c).items()
    
    for k, v in result:
        return k