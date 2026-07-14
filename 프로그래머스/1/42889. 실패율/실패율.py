def solution(N, stages):
    answer = []
    result = []
    left = len(stages)
    
    for i in range(N):
        if left-stages.count(i) != 0:
            left = left-stages.count(i)
            answer.append(stages.count(i+1) / left)
        else:
            answer.append(0)
    
    result=sorted(range(1, N+1), key=lambda x: answer[x-1], reverse=True)

    return result