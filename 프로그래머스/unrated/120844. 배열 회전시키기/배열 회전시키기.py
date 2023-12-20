def solution(numbers, direction):
    if direction == "right":
        numbers.insert(0, numbers.pop())
        return numbers
    
    s = numbers[0]
    del numbers[:1]
    numbers.append(s)
    
    return numbers