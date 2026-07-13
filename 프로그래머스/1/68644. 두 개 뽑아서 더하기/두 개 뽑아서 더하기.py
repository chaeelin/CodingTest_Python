def solution(numbers):
    answer = []
    
    for inx1 in range(len(numbers)):
        for inx2 in range(len(numbers)):
            if inx1 != inx2:
                answer.append(numbers[inx1] + numbers[inx2])
                
    answer = list(set(answer))
    answer.sort()
    
    return answer