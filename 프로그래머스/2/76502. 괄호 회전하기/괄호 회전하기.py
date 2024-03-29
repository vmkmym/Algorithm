def solution(s):
    answer = 0
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        if is_valid(rotated):
            answer += 1
    return answer

def is_valid(s):
    stack = []
    for char in s:
        if char in ['(', '[', '{']:
            stack.append(char)
        else:
            if not stack:
                return False
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
    return len(stack) == 0

# 올바른 괄호인지 확인하는 함수 + 괄호 한 칸씩 회전하는 함수