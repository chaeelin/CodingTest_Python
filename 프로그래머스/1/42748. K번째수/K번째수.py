def solution(array, commands):
    answer = []
    arrays = []
    
    for i in commands:
        arrays = array[i[0]-1:i[1]]
        arrays.sort()
        answer.append(arrays[i[2]-1])
        
    return answer