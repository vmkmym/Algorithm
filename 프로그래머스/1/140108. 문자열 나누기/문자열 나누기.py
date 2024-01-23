def solution(s):
    result = 0
    while s:
        x = s[0]
        cnt_x = cnt_y = 0
        for i, char in enumerate(s):
            if char == x:
                cnt_x += 1
            else:
                cnt_y += 1
            if cnt_x == cnt_y:
                result += 1
                s = s[i+1:]
                break
        else: 
            result += 1 # x와 y의 개수가 같아지지 않았을 때
            break
    return result