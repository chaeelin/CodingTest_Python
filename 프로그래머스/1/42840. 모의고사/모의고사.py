def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    first_count = 0 
    second_count = 0 
    third_count = 0 
    
    for i,answer in enumerate(answers):
        if answer == first[i%len(first)]:
            first_count += 1
        if answer == second[i%len(second)]:
            second_count += 1
        if answer == third[i%len(third)]:
            third_count += 1
    
    answer = []
    if first_count == max(first_count,second_count,third_count):
        answer.append(1)
    if second_count == max(first_count,second_count,third_count):
        answer.append(2)
    if third_count == max(first_count,second_count,third_count):
        answer.append(3)
    
    answer.sort()    
    return answer