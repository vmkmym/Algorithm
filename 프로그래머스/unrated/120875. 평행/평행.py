from itertools import combinations

def get_inclination(dot0, dot1):
    return abs(dot0[1] - dot1[1]) / abs(dot0[0] - dot1[0])

def solution(dots):
    for a, b in combinations(combinations(dots, 2), 2):
        # Check if the two sets of points have any common elements
        if not any(point in a for point in b):
            # Calculate inclination for the two pairs of points
            if get_inclination(*a) == get_inclination(*b):
                return 1
    return 0