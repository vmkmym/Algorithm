def solution(name, yearning, photo):
    memory = dict(zip(name, yearning))
    result = []

    for photo_list in photo:
        result.append(sum(memory.get(name, 0) for name in photo_list))

    return result