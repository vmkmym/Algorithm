def solution(chicken):
    order = 0 
    service = 0 

    while chicken > 0:
        chicken -= 1
        order += 1
        
        if order >= 10:
            service += 1
            order -= 10
            order += 1
    
    return service


# 다른 풀이 : 이게 뭔데...
def solution(chicken):
    return int(chicken*0.11111111111)