class Beverage:
    def __init__(self, name, size):
        self.name = name
        self.caffeine = 0
        self.size = size
        
    def __repr__(self):
        return f'{self.name} drink'
    
    def contains_caffeine(self):
        if (self.caffeine):
            return f'Contains {self.caffeine}mg per cup'
        
class Coffee(Beverage):
    def __init__(self, size='Small', name='Coffee'):
        super().__init__(size, name)
        self.caffeine = 125
        
    def price(self):
        return 5000
    
class Milk(Beverage):
    def __init__(self, size='Small', name='Milk'):
        super().__init__(size, name)
        self.caffeine = 0
        
    def price(self):
        return 3000
    
class CafeLatte(Coffee, Milk):
    def __init__(self, size):
        super().__init__(size, "CafeLatte")
        
'''
1. Coffee 클래스를 만들 때는 size 인자를 반드시 사용해야 한다
-> 그렇다. Coffee 클래스의 __init__ 메소드는 size 인자가 필요로 함.

2. CafeLatte 클래스를 만들 때는 size 인자를 반드시 사용해야 한다
-> 그렇다. CafeLatte 클래스의 __init__ 메소드는 size 인자를 필요로 함.

3. CafeLatte 클래스의 객체에 대해 price()를 실행했을 때 반환값은 Coffee 클래스의 객체의 price()와 동일하게 5000이다
-> 아니다. CafeLatte 클래스는 price 메소드를 정의하지 않았으므로, 상속받은 클래스의 price 메소드가 호출됨. 
Python은 다중 상속에서 메소드를 찾는 순서가 왼쪽에서 오른쪽이므로, Coffee 클래스의 price 메소드가 호출됨.

4. CafeLatte 클래스의 객체는 flavor 속성(attribute)을 가진다
-> 아니다. CafeLatte 클래스는 flavor 속성을 정의하지 않음.

5. CafeLatte 클래스의 객체의 caffeine 속성(attribute)의 값은 Milk와 동일한 0이다
-> 아니다. CafeLatte 클래스는 Coffee와 Milk 클래스를 상속받지만, __init__ 메소드에서 super()를 호출할 때 Coffee 클래스가 먼저 호출됨. 
따라서 CafeLatte 객체의 caffeine 속성은 Coffee 클래스의 caffeine 값인 125를 가짐.
'''