def solution(routes):
    number_of_camera = 0
    routes.sort(key=lambda x:x[1])
    camera_position = -30001
    for route in routes:
        if camera_position < route[0]:
            number_of_camera += 1
            camera_position = route[1] 
    return number_of_camera