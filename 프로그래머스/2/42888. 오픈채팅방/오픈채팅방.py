def solution(record):
    user = {}
    message = []
    for rec in record:
        rec = rec.split()
        if rec[0] == 'Enter':
            user[rec[1]] = rec[2]
            message.append([rec[1], "님이 들어왔습니다."])
        elif rec[0] == 'Leave':
            message.append([rec[1], "님이 나갔습니다."])
        elif rec[0] == 'Change':
            user[rec[1]] = rec[2]
    return [user[i[0]] + i[1] for i in message]