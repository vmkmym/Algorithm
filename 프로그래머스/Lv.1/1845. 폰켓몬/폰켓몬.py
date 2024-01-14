def solution(poketmon):
    poketmon_num = len(set(poketmon))
    return min(poketmon_num, len(poketmon) // 2)