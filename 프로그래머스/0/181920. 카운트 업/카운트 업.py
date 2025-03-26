def solution(start_num, end_num):
    answer = [start_num]
    for i in range(end_num-start_num+1):
        if i == 0:
            continue
        else:
            answer.append(start_num+i)
    return answer