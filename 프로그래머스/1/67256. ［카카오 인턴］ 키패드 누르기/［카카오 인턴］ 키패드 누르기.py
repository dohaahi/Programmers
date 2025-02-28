def solution(numbers, hand):
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    left_hand = keypad['*']
    right_hand = keypad['#']

    answer = ''

    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            left_hand = keypad[n]
        elif n in [3, 6, 9]:
            answer += 'R'
            right_hand = keypad[n]
        else:
            left = abs(left_hand[0] - keypad[n][0]) + abs(left_hand[1] - keypad[n][1])
            right = abs(right_hand[0] - keypad[n][0]) + abs(right_hand[1] - keypad[n][1])
            if left < right:
                answer += 'L'
                left_hand = keypad[n]
            elif left > right:
                answer += 'R'
                right_hand = keypad[n]
            else:
                if hand == 'left':
                    answer += 'L'
                    left_hand = keypad[n]
                else:
                    answer += 'R'
                    right_hand = keypad[n]

    return answer
