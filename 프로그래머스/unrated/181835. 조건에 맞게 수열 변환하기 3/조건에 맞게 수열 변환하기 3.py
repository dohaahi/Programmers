def solution(arr, k):
    if k % 2 != 0:
        return list(map(lambda a: a * k, arr))

    return list(map(lambda a: a + k, arr))