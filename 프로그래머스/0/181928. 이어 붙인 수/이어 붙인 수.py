def solution(num_list):
    m = len(num_list)
    answer1 = ""
    answer2 = ""
    
    for i in range(m):
        if num_list[i] % 2 == 0: 
            answer1 += str(num_list[i])
        else:
            answer2 += str(num_list[i])
        
    return int(f"{answer1}")+int(f"{answer2}")