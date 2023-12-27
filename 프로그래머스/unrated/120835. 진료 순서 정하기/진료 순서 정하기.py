def solution(emergency):
    answer = []

    sorted_array = sorted(emergency)
    for s in emergency:
        answer.append(len(emergency) - sorted_array.index(s))

    return answer