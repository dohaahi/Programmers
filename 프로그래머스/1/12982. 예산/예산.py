def solution(d, budget):
    answer = 0
    count = 0

    d.sort()
    
    for num in d:
        answer += num

        if answer > budget:
            return count
        count += 1

    return count