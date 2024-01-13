from collections import Counter

def solution(want, number, discount):
    grocery = Counter(item for item, count in zip(want, number) for _ in range(count))
    count = 0

    for i in range(len(discount)-9):
        if grocery == Counter(discount[i:i+10]):
            count += 1

    return count if count > 0 else 0