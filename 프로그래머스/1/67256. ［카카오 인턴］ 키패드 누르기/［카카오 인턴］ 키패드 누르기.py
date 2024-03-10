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

# 다른 사람의 풀이
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)} # 키패드 위치 딕셔너리화

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*' # 왼손의 초기 위치
    rhand = '#' # 오른손의 초기 위치
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i # 왼손의 현재 위치 업데이트
        elif i in right:
            answer += 'R'
            rhand = i # 오른손의 현재 위치 업데이트
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1]) # 왼손과의 거리 계산 후 저장 후 다음 반복 시 사용
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1]) # 오른손과의 거리 계산 후 저장 후 다음 반복 시 사용

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer