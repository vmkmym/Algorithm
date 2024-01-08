def solution(x):
    n = str(x) 
    num = 0
    
    for i in n:
        num += int(i)
        
    return x % num == 0 

# 하샤드 수(Harshad number)는 자연수를 그 자신을 이루는 각 자리의 숫자들의 합으로 나누어 떨어지는 수