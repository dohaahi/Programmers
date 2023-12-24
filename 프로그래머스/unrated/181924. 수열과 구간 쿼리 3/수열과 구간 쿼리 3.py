def solution(arr, queries):
    for q in queries:
        a = arr[q[0]]
        b = arr[q[1]]
        arr[q[1]] = a
        arr[q[0]] = b

    return arr