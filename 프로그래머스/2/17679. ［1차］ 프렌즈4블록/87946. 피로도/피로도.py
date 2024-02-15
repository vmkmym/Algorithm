import itertools

def solution(k, dungeons):
    orders = list(itertools.permutations(dungeons))
    max_dungeons = 0
    
    for order in orders:
        energy = k
        count = 0
        for dungeon in order:
            if energy >= dungeon[0]:
                energy -= dungeon[1] 
                count += 1 
            else:
                break 
        max_dungeons = max(max_dungeons, count) 

    return max_dungeons