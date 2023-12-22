def solution(code):
    ret = []
    mode = 0

    for idx in range(len(code)):
        if (mode == 0 and code[idx] != '1' and idx % 2 == 0) or (mode == 1 and code[idx] != '1' and idx % 2 == 1):
            ret.append(code[idx])
        elif code[idx] == '1':
            mode = 1 - mode

    return ''.join(ret) if ret else "EMPTY"

# 다른 사람 풀이
def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"

# code.split("1"): 입력된 문자열을 '1'을 기준으로 분할하여 리스트로 변환
# "".join(code.split("1"))[::2]: 분할된 문자열 리스트에서 짝수 번째 문자열을 가져와 이어붙임
# or "EMPTY": 위에서 만든 문자열이 비어있다면("".join(code.split("1"))[::2]가 False인 경우), "EMPTY"를 반환


