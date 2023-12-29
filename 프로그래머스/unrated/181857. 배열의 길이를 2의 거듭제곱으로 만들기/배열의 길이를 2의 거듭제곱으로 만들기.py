def solution(arr):
    answer = [1,2,4,8,16,32,64,128,256,512,1024]
    
    if len(arr) not in answer:
        for n in answer:
            if len(arr) < n:
                arr+= [0] * (n - len(arr))
                return arr


    return arr