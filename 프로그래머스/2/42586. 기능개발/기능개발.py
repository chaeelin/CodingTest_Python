import math

def solution(progresses, speeds):
    answer = []
    remainingTime = []
    
    for p, s in zip(progresses, speeds):
        remainingTime.append(math.ceil((100 - p) / s))
    
    count = 1
    
    if not remainingTime:
        return null

    currentTime = remainingTime[0]
    
    for i in range(1, len(remainingTime)):
        if remainingTime[i] <= currentTime:
            count += 1
        else:
            answer.append(count)
            count = 1
            currentTime = remainingTime[i]
    
    answer.append(count)
    
    return answer
