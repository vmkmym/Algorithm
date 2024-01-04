def solution(date1, date2):
    day1 = date1[0] * 365 + date1[1] * 30 + date1[2]
    day2 = date2[0] * 365 + date2[1] * 30 + date2[2]

    return 1 if day1 < day2 else 0