import sys

data = sys.stdin.readlines()

count = int(data[0])
m = int(data[1])
numbers = sorted(list(map(int, data[2].split())))

answer = 0
left = 0
right = count - 1

while left != right:
    sum_n = numbers[left] + numbers[right]
    if sum_n > m:
        right -= 1
    elif sum_n < m:
        left += 1
    else:
        left += 1
        answer += 1

print(answer)
