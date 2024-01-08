def solution(sizes):
    max_width = max(max(size) for size in sizes)
    max_height = max(min(size) for size in sizes)
    
    return max_width * max_height

# 다른 사람 풀이
# 모든 사이즈들을 하나의 리스트로 평탄화하는 sum(sizes, [])
solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)