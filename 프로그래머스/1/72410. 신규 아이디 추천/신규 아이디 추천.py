def solution(new_id):
    '''
    1단계: 모든 대문자를 소문자로 치환
    2단계: 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
    3단계: 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    4단계: 마침표(.)가 처음이나 끝에 위치한다면 제거
    5단계: new_id가 빈 문자열이라면 "a" 대입
    6단계: new_id의 길이가 16자 이상이면, 첫 15개의 문자를 제외한 나머지 문자 제거
    7단계: new_id의 길이가 2자 이하라면, 마지막 문자를 반복해서 끝에 붙임
    '''
    new_id = new_id.lower()
    
    new_id = ''.join(c for c in new_id if c.islower() or c.isdigit() or c in ['-', '_', '.'])
    
    temp_id = ''
    prev = ''
    for c in new_id:
        if c == '.' and prev == '.': # 현재 문자, 이전 문자가 마침표라면
            continue
        temp_id += c # 현재 문자를 추가
        prev = c # 이전 문자를 현재 문자로 할당
    new_id = temp_id
    
    # strip 메서드 : 문자열 앞 뒤의 지정한 매개변수 제거 (매개변수 없으면 공백)
    new_id = new_id.strip(".")
    
    if not new_id:
        new_id = "a"
    
    # 문자열 오른쪽 끝 지정한 매개변수 제거 (매개변수 없으면 공백)
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip(".")
    
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id