def solution(arr, queries):
    for q in queries:
        for qq in range(q[0],q[1]+1):
            arr[qq] += 1

    return arr