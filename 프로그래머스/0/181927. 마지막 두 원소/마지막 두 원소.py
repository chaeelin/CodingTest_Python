def solution(num_list):
    n = len(num_list)-1
    if (num_list[n] > num_list[n-1]):
        num_list.append(int(num_list[n]) - int(num_list[n-1]))
    else:
        num_list.append(int(num_list[n])*2)
    return num_list