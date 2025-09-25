from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        cur = prices.popleft()
        t = 0
        for i in prices:
            t += 1
            if i < cur:
                break
        answer.append(t)
    return answer