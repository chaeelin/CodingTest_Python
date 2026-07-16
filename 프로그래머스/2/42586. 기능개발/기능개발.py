def solution(progresses, speeds):
    answer = []
    stack = []
    count = 1
    
    for i in range(len(progresses)):
        if ((100-progresses[i]) % speeds[i] > 0):
            stack.append(((100-progresses[i]) // speeds[i])+1)
        else:
            stack.append((100-progresses[i]) // speeds[i])
    
    current = stack[0]
    
    for i in range(len(stack)-1):
        if current >= stack[i+1]:
            count +=1
        else:
            answer.append(count)
            current = stack[i+1]
            count = 1
            
    answer.append(count)
    
    return answer