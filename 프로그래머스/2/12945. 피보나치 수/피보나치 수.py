def solution(n):
    fn = [0, 1] # 초기항 F(0) = 0, F(1) = 1일 때
    
    for i in range(2, n+1):
        fibonacci = (fn[i - 1] + fn[i - 2]) % 1234567
        fn.append(fibonacci)
        
    return fn[n]
