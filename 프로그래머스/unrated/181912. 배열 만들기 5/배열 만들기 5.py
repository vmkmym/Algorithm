def solution(intStrs, k, s, l):
    return [int(part[s:s + l]) for part in intStrs if int(part[s:s + l]) > k]
