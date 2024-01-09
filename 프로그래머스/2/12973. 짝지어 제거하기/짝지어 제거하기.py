def solution(s):
    stack = []
    
    for char in s:
        if not stack or char != stack[-1]:
            stack.append(char)
        else:
            stack.pop()
            
    return 1 if not stack else 0