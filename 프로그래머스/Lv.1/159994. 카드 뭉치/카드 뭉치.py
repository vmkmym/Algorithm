def solution(cards1, cards2, goal):
    i, j, k = 0, 0, 0
    while k < len(goal):
        if i < len(cards1) and cards1[i] == goal[k]:
            i += 1
        elif j < len(cards2) and cards2[j] == goal[k]:
            j += 1
        else:
            return "No"
        k += 1
    return "Yes"