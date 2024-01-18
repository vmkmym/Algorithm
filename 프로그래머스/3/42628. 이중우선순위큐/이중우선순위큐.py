def solution(operations):
    queue = []
    for operation in operations:
        op, num = operation.split()
        if op == 'I':
            queue.append(int(num))
        elif queue:
            if num == '1':
                queue.remove(max(queue))
            else:
                queue.remove(min(queue))
    return [0, 0] if not queue else [max(queue), min(queue)]