def solution(keymap, targets):
    keyPressCount = {}
    for _, key in enumerate(keymap, start=1):     # keymap의 key와 등장횟수를 저장
        for j, char in enumerate(key, start=1):
            if char not in keyPressCount or j < keyPressCount[char]:  # keyPressCount에 없거나 등장횟수가 더 작은 것을 저장
                keyPressCount[char] = j
    
    result = []
    for target in targets:     # target이 keyPressCount에 없으면 -1, 있으면 등장횟수를 더함
        count = 0
        for char in target:
            if char not in keyPressCount:
                count = -1
                break
            count += keyPressCount[char]
        result.append(count)
        
    return result