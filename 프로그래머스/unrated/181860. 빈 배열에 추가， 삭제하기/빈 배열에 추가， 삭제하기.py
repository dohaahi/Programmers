def solution(arr, flag):
    answer = []

    for i in range(len(arr)):
        if flag[i]:
            for s in range(arr[i]*2):
                answer.append(arr[i])
            continue
        for k in range(arr[i]):
            answer.pop()

    return answer