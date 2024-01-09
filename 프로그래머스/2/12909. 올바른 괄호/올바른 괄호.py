def solution(s):
    stack = []
    
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        elif not stack:
            return False
        else:
            stack.pop()
    
    return not stack