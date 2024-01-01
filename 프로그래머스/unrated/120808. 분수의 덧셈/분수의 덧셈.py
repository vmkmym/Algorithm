from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):    
    result = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    return [result.numerator, result.denominator]

# fractions 모듈은 유리수의 산술을 지원함. 
# Fraction 인스턴스는 한 쌍의 정수, 다른 유리수 또는 문자열로 만들 수 있습니다.
# numerator : 기약 분수로 나타낼 때 Fraction의 분자.
# denominator : 기약 분수로 나타낼 때 Fraction의 분모.
class fractions.Fraction(numerator=0, denominator=1)
class fractions.Fraction(other_fraction)
class fractions.Fraction(float)
class fractions.Fraction(decimal)
class fractions.Fraction(string)
