def solution(order):
    americano = sum(4500 for coffee in order if 'latte' not in coffee)
    latte = sum(5000 for coffee in order if 'latte' in coffee)
    return americano + latte