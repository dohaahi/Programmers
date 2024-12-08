import sys

count, total_sum = map(int, sys.stdin.readline().split(' '))
nums = list(map(int, sys.stdin.readline().split(' ')))

start_p, end_p = 0, 0

answer = 0
current_sum = 0
while end_p < count:

    current_sum += nums[end_p]

    while current_sum > total_sum:
        current_sum -= nums[start_p]
        start_p += 1

    if current_sum == total_sum:
        answer += 1
    end_p += 1

print(answer)
