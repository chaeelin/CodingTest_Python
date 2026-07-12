def solution(numbers):
    answer = []
    
    for idx1 in range(len(numbers)):
        for idx2 in range(len(numbers)):
            if idx1 == idx2:
                pass
            else:
                result = numbers[idx1]+numbers[idx2]
                answer.append(result)
    answer = list(set(answer))
    answer.sort()
    return answer