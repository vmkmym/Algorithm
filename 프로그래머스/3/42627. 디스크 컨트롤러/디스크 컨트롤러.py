import heapq

def solution(jobs):
    # 작업을 시작 시간과 소요 시간 순으로 정렬
    jobs.sort(key=lambda x: (x[0], x[1]))
    total_time = 0
    current_time = 0
    total_jobs = len(jobs)
    waiting_jobs = [] # 대기 중인 작업들
    
    while jobs or waiting_jobs: 
        # 현재 시간 이전에 요청된 작업들을 대기 작업 리스트에 추가
        while jobs and jobs[0][0] <= current_time:
            job = heapq.heappop(jobs)
            heapq.heappush(waiting_jobs, (job[1], job[0])) # 소요 시간이 짧은 순으로 대기 작업 리스트에 추가
            
        if waiting_jobs:
            # 대기 작업 리스트에서 소요 시간이 가장 짧은 작업을 선택
            take_time, request_time = heapq.heappop(waiting_jobs)
            current_time += take_time
            total_time += current_time - request_time
        else:
            # 대기 작업이 없는 경우, 다음 작업의 시작 시간으로 현재 시간을 설정
            current_time = max(current_time, jobs[0][0])
            
    return total_time // total_jobs