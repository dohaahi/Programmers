def solution(arr):
    stk = []

    for i in range(len(arr)):
        if not stk:
            stk.append(arr[i])
        elif stk[-1] == arr[i]:
            del stk[-1]
        else:
            stk.append(arr[i])

    return [-1] if not stk else stk