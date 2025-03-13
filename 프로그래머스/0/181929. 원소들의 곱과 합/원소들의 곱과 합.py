def solution(num_list):
    answer1 = pow(sum(num_list),2)
    answer2 = 1

    m = len(num_list)
    for i in range(m):
        answer2 = answer2 * num_list[i]
        
    if answer1 > answer2:
        return 1
    else:
        return 0