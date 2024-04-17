def solution(today, terms, privacies):
    term_validity = {}  # 약관별 유효 기간 저장
    for term in terms:
        term_name, duration = term.split()
        term_validity[term_name] = int(duration)
    
    answer = []
    
    for idx, privacy in enumerate(privacies):
        collection_date, term = privacy.split()
        year, month, day = map(int, collection_date.split('.'))
        
        term_duration = term_validity[term]  # term에 따른 유효 기간
        expiry_year = year + (month + term_duration - 1) // 12
        expiry_month = (month + term_duration - 1) % 12 + 1
        expiry_date = f"{expiry_year:04d}.{expiry_month:02d}.{day:02d}"
        
        if expiry_date <= today:
            answer.append(idx + 1)  # 개인정보 번호는 1부터 시작하므로 idx + 1 추가
    
    return answer