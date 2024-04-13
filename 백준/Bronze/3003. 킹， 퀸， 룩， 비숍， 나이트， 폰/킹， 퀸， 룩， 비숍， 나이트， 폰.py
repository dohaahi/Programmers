nums = input().split(' ')

chess = [1, 1, 2, 2, 2, 8]

answer = []
for i in range(len(nums)):
    answer.append(chess[i] - int(nums[i]))

print(' '.join(map(str, answer)))
