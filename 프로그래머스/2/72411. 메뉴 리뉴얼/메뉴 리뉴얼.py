from itertools import combinations # 조합
from collections import Counter # 카운터

def solution(orders, course):
    '''
    1. course를 순회한다
        2. orders를 순회한다
            3. orders의 각 원소를 정렬한다
            4. orders의 각 원소를 course의 원소만큼 조합한다
        5. Counter를 이용하여 각 메뉴의 조합의 개수를 센다
        6. 가장 많이 나온 메뉴의 조합에 대해
            7. count가 1보다 크고, count가 가장 많이 나온 메뉴의 조합과 같다면
                8. result에 해당 조합의 메뉴를 추가한다
    9. result를 정렬하여 반환한다
    '''
    result = []
    for num_of_dishes in course:
        menu_combination = []
        for order in orders:
            menu_combination += combinations(sorted(order), num_of_dishes)
        menu_counter = Counter(menu_combination).most_common()
        
        for menu, count in menu_counter:
            if count > 1 and count == menu_counter[0][1]:
                result.append(''.join(menu))
    return sorted(result)