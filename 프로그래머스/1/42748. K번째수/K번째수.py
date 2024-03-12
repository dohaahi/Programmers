def solution(array, commands):
    answer = []

    for nums in commands:
        new_num = sorted(array[nums[0]-1: nums[1]])
        answer.append(new_num[nums[2]-1])

    return answer