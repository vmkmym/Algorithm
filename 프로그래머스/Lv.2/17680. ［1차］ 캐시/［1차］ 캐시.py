from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0: # 캐시사이즈가 0이면 모두 miss
        return len(cities) * 5
    
    cache = deque()
    answer = 0
    
    for city in cities: # 캐시에 있는지 없는지 확인
        city = city.lower() 
        if city in cache: # 캐시에 있으면
            cache.remove(city) # 캐시에서 제거
            cache.append(city) # 캐시에 추가
            answer += 1 # 캐시에서 찾았으니 1
        else: # 캐시에 없으면
            if len(cache) == cacheSize: # 캐시가 꽉 찼으면
                cache.popleft() # 가장 오래된 캐시 제거
            cache.append(city) # 캐시에 추가
            answer += 5 # 캐시에 없으니 5
    return answer 