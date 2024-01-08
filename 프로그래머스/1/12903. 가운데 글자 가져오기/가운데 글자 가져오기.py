def solution(s):
    length = len(s)
    char = length // 2

    return s[char-1 : char+1] if length % 2 == 0 else s[char]