from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque([(begin, 0)]) # (단어, 경로)

    while queue:
        current, depth = queue.popleft()
        if current == target:
            return depth
        for word in words:
            if sum([a!=b for a, b in zip(current, word)]) == 1: # 한 글자만 다른 경우
                queue.append((word, depth + 1)) # 현재 단어를 한 글자만 바꿔서 다른 단어로 변환할 수 있는 경우 큐에 추가
                words.remove(word) # 방문한 단어는 제거
    return 0

# 너비 우선 탐색(BFS) 알고리즘