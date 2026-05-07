def solution(numbers):
    result = 0
    answer = []
    
    for i,num in enumerate(numbers):
        for j,num1 in enumerate(numbers):
            if j == i:
                pass
            else:
                result = num+num1
                answer.append(result)
                
    answer = list(set(answer)) 
    answer.sort()
    return answer