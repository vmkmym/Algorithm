def solution(lottos, win_nums):
    match_count = 0
    zero_count = 0

    for num in lottos:
        if num == 0:
            zero_count += 1
        elif num in win_nums:
            match_count += 1

    highest_rank = 7 - (match_count + zero_count)
    lowest_rank = 7 - match_count

    if highest_rank > 6:
        highest_rank = 6
    if lowest_rank > 6:
        lowest_rank = 6

    return [highest_rank, lowest_rank]