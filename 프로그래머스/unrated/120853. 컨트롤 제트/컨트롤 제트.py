def solution(s):
    result = 0
    stack = s.split()

    for i in range(len(stack)):
        if stack[i] == "Z":
            result -= int(stack[i-1])
        else:
            result += int(stack[i])

    return result