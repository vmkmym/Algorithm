def solution(quiz):
    results = []

    for monomial in quiz:
        equation = monomial.replace('=', '==')  # 등호를 비교 연산자로 바꿈 
        if eval(equation):
            results.append("O")
        else:
            results.append("X")

    return results

# "3 - 4 = -3" 같은 수식은 변수 할당을 나타내므로 eval() 함수로 직접 실행X