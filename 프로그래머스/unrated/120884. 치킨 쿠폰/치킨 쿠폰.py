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