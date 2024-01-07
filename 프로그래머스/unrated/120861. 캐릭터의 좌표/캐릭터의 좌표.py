def solution(keyinput, board):
    x, y = 0, 0
    x_axis, y_axis = board[0] // 2, board[1] // 2
    
    for key in keyinput:
        if key == 'left' and x > -x_axis:
            x -= 1
        elif key == 'right' and x < x_axis:
            x += 1
        elif key == 'down' and y > -y_axis:
            y -= 1
        elif key == 'up' and y < y_axis:
            y += 1

    return [x, y]