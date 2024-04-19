nums = []

for _ in range(9):
    num_list = input().split()
    for n in num_list:
        nums.append(int(n))

max_num = max(nums)
index = nums.index(max_num)
print(f"{max_num}\n{index//9+1} {index%9+1}")
