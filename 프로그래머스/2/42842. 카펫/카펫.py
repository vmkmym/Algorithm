def solution(brown, yellow):
    carpet = brown + yellow
    
    for x in range(1, int(carpet ** 0.5) + 1):
        if carpet % x == 0:
            y = carpet // x
            if (x-2) * (y-2) == yellow:
                return [max(x, y), min(x, y)]
'''
완전탐색과 브루트포스 알고리즘은 문제 해결을 위해 가능한 모든 경우를 탐색하는 접근 방법이지만, 
일반적으로 완전탐색이라는 용어가 더 넓은 의미로 사용되며, 브루트포스 알고리즘은 그 중 하나의 구체적인 방법론을 가리킵니다.
'''
