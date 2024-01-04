def solution(picture, k):
    new_picture = []
    
    for tv in picture:
        new_tv = ''.join([pixel * k for pixel in tv])
        for _ in range(k):
            new_picture.append(new_tv)
            
    return new_picture
