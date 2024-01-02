def solution(money):
    ice = int(money) // 5500
    change = money - (ice * 5500)
    return [ice, change]