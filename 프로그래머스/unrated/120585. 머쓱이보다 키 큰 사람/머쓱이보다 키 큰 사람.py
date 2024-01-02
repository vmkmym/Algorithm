def solution(array, height):
    return sum(1 for tall in array if tall > height)