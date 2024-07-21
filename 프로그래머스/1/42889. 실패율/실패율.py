def solution(N, stages):
    people = len(stages)
    per = {}

    for i in range(1, N + 1):
        count = stages.count(i)
        if count != 0:
            per[i] = count / people
        else:
            per[i] = 0
        people -= count

    per = sorted(per.items(), key=lambda item: item[1], reverse=True)
    return [item[0] for item in per]