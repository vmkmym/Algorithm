import re

def solution(skill, skill_trees):
    count = 0
    for tree in skill_trees:
        tree = re.sub(f'[^{skill}]', '', tree)
        if skill.startswith(tree):
            count += 1
    return count

# 정규식 이용해서 skill에 없는 문자를 제거하고 (re.sub)
# skill의 시작이 tree의 시작과 같은지 비교 (startswith)