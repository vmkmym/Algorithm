def solution(routes):
    number_of_camera = 0
    routes.sort(key=lambda x:x[1]) # 고속도로 진입 지점을 기준으로 정렬
    camera_position = -30001 # 카메라의 위치를 -30001(진입지점)로 초기화
    for route in routes:
        if camera_position < route[0]: # 카메라의 위치가 고속도로 진입 지점 route[i][0]보다 작다면 => 고속도로 진입 지점에 카메라가 없다면
            number_of_camera += 1 # 카메라의 개수를 1 증가 => 고속도로 진입 지점에 카메라를 설치
            camera_position = route[1] # 카메라의 위치를 카메라의 진출 지점으로 변경
    return number_of_camera