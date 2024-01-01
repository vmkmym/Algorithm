def solution(common):
    if common[1] - common[0] == common[-1] - common[-2]:  
        next_num = common[-1] + (common[1] - common[0])
    else:  
        next_num = common[-1] * (common[1] // common[0])
    return next_num


def solution2(common):
    if len(common) < 3:
        return None
    
    diff = common[2] - common[1]
    
    if diff == 0:  
        return common[-1]  
    
    if diff == 1 or diff == -1:  
        return common[-1] + diff
    
    if diff > 1 or diff < -1:  
        ratio = common[2] // common[1] 
        return common[-1] * ratio
    
    return None  

# 공차가 0인 경우
# common의 원소가 음수인 경우
# 공차와 공비를 두번째와 첫번째로 해야됨