from collections import deque;

def solution(prices):
    prices_queue = deque(prices);
    answer = []

    while prices_queue:
        time_count = 0

        num1 = prices_queue.popleft()
        for num2 in prices_queue:
            time_count += 1
            if(num1 > num2): break

        answer.append(time_count)

    return answer

p = [1,2,3,2,3]
print(solution(p))


