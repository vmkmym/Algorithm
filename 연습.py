def solution(today, terms, privacies):
    '''
    today : 오늘 날짜
    terms : ["약관타입 유효기간"]
    privacies : ["수집일자 약관타입"]
    => 파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return 
    '''
    term_validity = {}  # 약관별 유효 기간 저장
    for term in terms:
        term_name, duration = term.split()
        term_validity[term_name] = int(duration) # 유효기간을 정수로 담기
    
    # 파기해야 할 개인정보의 번호를 담을 리스트
    answer = []
    
    for idx, privacy in enumerate(privacies):
        # 수집일자, 약관타입으로 분리
        collection_date, term = privacy.split()
        # 수집일자를 년, 월, 일로 분리해서 정수로 변환
        year, month, day = map(int, collection_date.split('.'))
        
        # 약관 타입에 따른 유효기간을 가져옴
        term_duration = term_validity[term]
        
        # 만료일 계산, 현재 연도 + (현재 월 + 유효기간 - 1) // 12, (현재 월 + 유효기간 - 1) % 12 + 1
        # 1을 빼는 이유는 현재 월을 포함해서 계산하기 때문
        expiry_year = year + (month + term_duration - 1) // 12
        expiry_month = (month + term_duration - 1) % 12 + 1
        
        # YYYY.MM.DD 형식으로 만료일을 저장
        expiry_date = f"{expiry_year:04d}.{expiry_month:02d}.{day:02d}"
        
        # 만약 만료일이 오늘 날짜보다 이전이라면 파기 리스트에 추가
        if expiry_date <= today:
            answer.append(idx + 1)  # 개인정보번호는 1부터 시작하므로 idx + 1 추가
    
    return answer