def solution(id_pw, db):
    for id, pw in db:
        if id == id_pw[0]:
            return "login" if pw == id_pw[1] else "wrong pw"
    return "fail"

# 다른 사람 풀이
# := 는 할당 표현식으로 변수에 표현식을 할당하는 것임
# 여기서는 pw 변수에 표현식을 할당
    # db 리스트를 dictionary로 만들어서 key를 .get(id_pw[0]) 로 가져오는 것임. 그래서 pw에는 key(id)에 맞는 값을 가져와서 할당해주고 없다면 None을 반환
def solution(id_pw, db):
    if pw := dict(db).get(id_pw[0]):
        return "login" if pw == id_pw[1] else "wrong pw"
    return "fail"
