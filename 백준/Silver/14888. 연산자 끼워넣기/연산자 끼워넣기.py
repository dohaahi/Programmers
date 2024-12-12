import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))

maximum = -1e9
minimum = 1e9


def dfs(i, answer, plus, minus, multiply, divide):
    global maximum, minimum

    if i == n:
        maximum = max(answer, maximum)
        minimum = min(answer, minimum)
        return

    if plus:
        dfs(i + 1, answer + nums[i], plus - 1, minus, multiply, divide)
    if minus:
        dfs(i + 1, answer - nums[i], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(i + 1, answer * nums[i], plus, minus, multiply - 1, divide)
    if divide:
        dfs(i + 1, int(answer / nums[i]), plus, minus, multiply, divide - 1)


dfs(1, nums[0], operator[0], operator[1], operator[2], operator[3])
print(maximum)
print(minimum)