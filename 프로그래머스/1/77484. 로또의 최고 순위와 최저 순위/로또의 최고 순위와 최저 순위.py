def solution(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]
    cnt_0 = lottos.count(0)
    ans = len(set(win_nums) & set(lottos))
    return rank[cnt_0 + ans], rank[ans]