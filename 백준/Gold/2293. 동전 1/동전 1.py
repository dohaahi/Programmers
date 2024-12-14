import sys

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readlines()) )
answer = 0

dp = [0 for _ in range(k + 1)]
dp[0] = 1

for n in nums:
    for i in range(n, k + 1):
        dp[i] = dp[i] + dp[i - n]

print(dp[-1])
