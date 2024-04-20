answer = []
nums = []

input_num = list(map(int, input().split()))

while input_num != [0, 0, 0]:
    nums.append(input_num)
    input_num = list(map(int, input().split()))

for num in nums:
    a, b, c = sorted(num)
    if c ** 2 == a ** 2 + b ** 2:
        answer.append('right')
    else:
        answer.append('wrong')

for a in answer:
    print(a)
