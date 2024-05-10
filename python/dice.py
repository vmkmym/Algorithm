import random

class Dice():
    def __init__(self, num_side, condition):
        self.num_side = num_side
        self.condition = condition
        
    def roll(self):
        score = random.randrange(self.num_side) + 1
        if not self.condition(score):
            raise 1
        return score
    
even_dice = Dice(6, lambda x: x % 2 == 0) 
try:
    total_score = 0
    for _ in range(3):
        total_score += even_dice.roll()
    print('Win!')
except:
    print('Lose!')
finally:
    print('Total:', total_score)
    
'''
다음 코드를 실행했을 때 두 번째 줄에 “Total: 6”이 출력되었습니다. 
이 때 첫 번째 줄이 “Win!”이었을 확률은?
1/8
'''