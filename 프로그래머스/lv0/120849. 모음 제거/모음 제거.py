def solution(my_string):
    al = {'a', 'e', 'i', 'o', 'u'}

    for i in al:    
        my_string = my_string.replace(i, "")

    return my_string