def solution(code):
    ret = []
    mode = 0

    for idx in range(len(code)):
        if (mode == 0 and code[idx] != '1' and idx % 2 == 0) or (mode == 1 and code[idx] != '1' and idx % 2 == 1):
            ret.append(code[idx])
        elif code[idx] == '1':
            mode = 1 - mode

    return ''.join(ret) if ret else "EMPTY"