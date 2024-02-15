def solution(poketmon):
    return min(len(set(poketmon)), len(poketmon) // 2)

# 해시
# 해시는 데이터를 저장, 검색, 삭제 등을 효율적으로 수행할 수 있도록 도와주는 자료구조
# 해시는 키(key)와 값(value)을 하나의 데이터로 저장하는 자료구조 (Python의 Dictionary 타입이 해시 테이블과 같은 구조)
# 키는 해시 함수를 통해 고유한 해시값으로 변환되고 이 해시값은 데이터가 저장되는 위치(index)를 결정한다.