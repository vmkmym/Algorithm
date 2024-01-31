def solution(order):
    sub_container = []
    box_count = 0
    idx = 0

    for box in range(1, len(order) + 1):
        sub_container.append(box)
        while sub_container and sub_container[-1] == order[idx]:
            sub_container.pop()
            idx += 1
            box_count += 1

    return box_count