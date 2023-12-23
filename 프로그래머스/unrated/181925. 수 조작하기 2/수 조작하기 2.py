def solution(numLog):
    return "".join(["w" if numLog[i] - numLog[i - 1] == 1 else "s" if numLog[i] - numLog[i - 1] == -1 else "d" if numLog[i] - numLog[i - 1] == 10 else "a" for i in range(1, len(numLog))])
