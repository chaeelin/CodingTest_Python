def solution(n):
    answer = []
    
    def hanoi(n,start,layover,destion):
        if n == 1:
            answer.append([start,destion])
        else:
            hanoi(n-1, start, destion, layover)
            answer.append([start, destion])
            hanoi(n-1, layover, start, destion)
            
    hanoi(n, 1, 2, 3)         
    return answer