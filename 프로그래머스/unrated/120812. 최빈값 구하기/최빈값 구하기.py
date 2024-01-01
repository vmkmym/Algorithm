import statistics

def solution(array):
    modes = statistics.multimode(array)
    return -1 if len(modes) > 1 else modes[0]
    
