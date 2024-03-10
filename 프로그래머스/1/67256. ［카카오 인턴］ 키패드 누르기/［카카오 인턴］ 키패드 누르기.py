def solution(numbers, hand):
    answer = ''
    keypad = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    hand_positions = {'L': [3, 0], 'R': [3, 2]}

    def press_button(num, hand):
        nonlocal answer
        hand_positions[hand] = keypad[num]
        answer += hand

    for num in numbers:
        if num in [1, 4, 7]:
            press_button(num, 'L')
        elif num in [3, 6, 9]:
            press_button(num, 'R')
        else:
            left_dist = sum(abs(a-b) for a, b in zip(hand_positions['L'], keypad[num]))
            right_dist = sum(abs(a-b) for a, b in zip(hand_positions['R'], keypad[num]))

            if left_dist < right_dist or (left_dist == right_dist and hand == 'left'):
                press_button(num, 'L')
            else:
                press_button(num, 'R')

    return answer