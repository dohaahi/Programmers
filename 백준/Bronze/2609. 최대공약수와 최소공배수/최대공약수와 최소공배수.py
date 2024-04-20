n, m = sorted(list(map(int, input().split())))
answer = [1, 1]
mul = n * m

for i in range(2, n + 1):
    while n % i == 0 and m % i == 0:
        n //= i
        m //= i
        answer[0] *= i
answer[1] = mul // answer[0]

print(*answer)
