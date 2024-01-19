def solution(msg):
    dic = {chr(i + 64): i for i in range(1, 27)} # 주어진 숫자 i에 해당하는 ASCII 문자를 반환
    next_index = 27

    result = []
    w = msg[0]
    for c in msg[1:]:
        wc = w + c
        if wc in dic:
            w = wc
        else:
            result.append(dic[w])
            dic[wc] = next_index
            next_index += 1
            w = c

    result.append(dic[w])
    return result