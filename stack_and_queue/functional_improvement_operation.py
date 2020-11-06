import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    days = []

    #day 구하기
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i]) #올림하기
        days.append(day)

    days_queue = deque(days)

    base = days_queue.popleft()
    cnt = 1

    while days_queue:
        next = days_queue[0]

        if (base < next):
            base = days_queue.popleft()
        else:
            cnt += 1
            days_queue.popleft()
            continue
        answer.append(cnt)
        cnt = 1 # 초기화
    answer.append(cnt)

    return answer


p = [95, 90, 99, 99, 80, 99]
s = [1, 1, 1, 1, 1, 1]
print(solution(p,s))