import itertools


def solution(nums):
    answer = 0

    for i in itertools.combinations(nums, 3):
        is_prime = True
        for j in range(2, int(sum(i) ** 0.5) + 1):
            if sum(i) % j == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1

    return answer