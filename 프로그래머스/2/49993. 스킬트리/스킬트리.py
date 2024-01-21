import re

def solution(skill, skill_trees):
    count = 0
    for tree in skill_trees:
        tree = re.sub(f'[^{skill}]', '', tree)
        if skill.startswith(tree):
            count += 1
    return count
