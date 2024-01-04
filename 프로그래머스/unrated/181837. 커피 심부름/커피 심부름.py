def solution(order):
    americano = {"iceamericano", "americanoice", "hotamericano", "americanohot", "americano", "anything"}
    latte = {"icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte"}
    
    black = sum(1 for coffee in order if coffee in americano)
    milk = len(order) - black
    
    return black * 4500 + milk * 5000