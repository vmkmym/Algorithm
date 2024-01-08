def solution(price, money, count):
    pay = 0
    
    for c in range(1, count+1):
        pay += c * price
        
    return 0 if pay < money else pay-money