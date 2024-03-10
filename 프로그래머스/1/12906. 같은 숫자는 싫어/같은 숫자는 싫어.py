def solution(arr):
    answer = []

    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[0])
            
        if answer[-1] != arr[i]:
            answer.append(arr[i])

    return answer