def solution(n, lost, reserve):
    answer = 0
    d = {}
    
    for i in range(1,n+1):
        if i not in lost:
            d[i] = 1
        else:
            d[i] = 0
        
        if i in reserve:
            d[i] += 1
    
    for i in range(1,n+1):
        if d[i] == 0:
            if i > 1 and d[i-1] == 2:
                d[i-1] -= 1
                d[i] += 1
            elif i < n and d[i+1] == 2:
                d[i+1] -= 1
                d[i] += 1
    
    for i in range(1, n+1):
        if d[i] >= 1:
            answer += 1

    return answer