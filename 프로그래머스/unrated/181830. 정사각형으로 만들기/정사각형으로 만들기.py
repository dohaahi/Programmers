def solution(arr):
    if len(arr) == len(arr[0]):
        return arr
    
    length = max(len(arr), len(arr[0]))

    if length != len(arr):
        zero = [0] * length
        for i in range((length - len(arr))):
            arr.append(zero) 
        return arr

    for inner in arr:
        for i in range((length - len(inner))):
            inner.append(0) 

    return arr