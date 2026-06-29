import math

def solution(progresses, speeds):
    answer = []
    days = []
    count = 1
    max = 0
    
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
        
    for i in range(len(days)-1):
        if max < days[i]:
            max = days[i]
            
        if days[i+1] > max:
            answer.append(count)
            count = 1
        else: count += 1
        
    answer.append(count)
                
    return answer