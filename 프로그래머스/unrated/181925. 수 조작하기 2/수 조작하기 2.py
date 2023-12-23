def solution(numLog):
    return "".join(["w" if numLog[i] - numLog[i - 1] == 1 else "s" if numLog[i] - numLog[i - 1] == -1 else "d" if numLog[i] - numLog[i - 1] == 10 else "a" for i in range(1, len(numLog))])

# 처음 풀이 : 이 문제는 다른 사람 풀이도 메모리랑 시간이 줄어들지가 않는데 왜지...
def solution(numLog):
    control = []
    for i in range(len(numLog)):
        if i > 0:
            diff = numLog[i] - numLog[i - 1]

            if diff == 1:
                control.append('w')
            elif diff == -1:
                control.append('s')
            elif diff == 10:
                control.append('d')
            elif diff == -10:
                control.append('a')   
    return ''.join(control)

# 딕셔너리 활용했을 때 
def solution(numLog):
    dict = {'1':'w', '-1':'s', '10':'d', '-10':'a'}
    word = ''
    for i in range(1, len(numLog)):
        word += dict[str(numLog[i] - numLog[i - 1])]
    return word

