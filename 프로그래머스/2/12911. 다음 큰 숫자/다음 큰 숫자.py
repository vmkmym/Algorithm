def solution(n):
    binary = format(n, 'b')
    n_count = binary.count('1')
    m = n+1
    
    while True:
        m_bin = format(m, 'b')
        m_count = m_bin.count('1')
        
        if m_count == n_count:
            return m
        
        m += 1
    
    return m