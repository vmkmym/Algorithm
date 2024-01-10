n, m = map(int, input().split())
try:
    weights = list(map(int, input().split()))
    box = 1
    total_weight = 0

    for weight in weights:
        if weight > m:
            print(0)
        if total_weight + weight > m:
            box += 1
            total_weight = weight
        else:
            total_weight += weight
            
    if n == 0:
        print(0)
    else:
        print(box)
except:
    print(0)