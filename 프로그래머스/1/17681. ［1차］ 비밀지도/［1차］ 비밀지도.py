def solution(n, arr1, arr2):
    answer = []

    # 1. 정수 배열을 돌며 각 숫자를 2진수로 나타내기
    # 2. 배열1과 배열2를 or 연산을 통해 하나의 배열로 합치기
    # 3. 최종 배열 반환

    for i, j in zip(arr1, arr2):
        num1 = bin_fun(i,n)
        num2 = bin_fun(j,n)
        answer.append(or_fun(num1, num2))

    for i in range(len(answer)):
        answer[i] = answer[i].replace('1', '#').replace('0', ' ')

    return answer


def bin_fun(num,n):
    bin_num = format(num, 'b')
    if len(bin_num) != n:
        bin_num = '0' * (n - len(bin_num)) + bin_num
    return bin_num


def or_fun(num1, num2):
    new_num = ''

    for i, j in zip(num1, num2):
        new_num += str(int(i) | int(j))
    return new_num