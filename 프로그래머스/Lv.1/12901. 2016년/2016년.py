def solution(month, day):
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    return days[(sum(months[:month-1])+day-1)%7]