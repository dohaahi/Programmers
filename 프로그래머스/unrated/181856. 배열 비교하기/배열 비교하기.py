def solution(arr1, arr2):
    if len(arr1) > len(arr2):
        return 1
    elif len(arr2) > len(arr1):
        return -1
        
    if sum(a for a in arr1) > sum(a for a in arr2):
        return 1
    elif sum(a for a in arr1) < sum(a for a in arr2):
        return -1
    
    return 0