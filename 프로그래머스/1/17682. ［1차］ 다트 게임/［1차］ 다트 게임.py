import re

def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'*': 2, '#': -1, '': 1}
    p = re.compile("(\d+)([SDT])([*#]?)") 
    dart = p.findall(dartResult) # [('1', 'D', ''), ('2', 'S', '#'), ('10', 'S', '')]
    
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
        
    return sum(dart)