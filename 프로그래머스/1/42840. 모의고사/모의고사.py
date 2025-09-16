def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    
    first_count, second_count, third_count = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == first[i % len(first)]:
            first_count += 1
        if answers[i] == second[i % len(second)]:
            second_count += 1 
        if answers[i] == third[i % len(third)]:
            third_count += 1 
        
    max_score = max(first_count, second_count, third_count)

    result = []
    if first_count == max_score:
        result.append(1)
    if second_count == max_score:
        result.append(2)
    if third_count == max_score:
        result.append(3)

    return result