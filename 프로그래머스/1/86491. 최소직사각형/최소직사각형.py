def solution(sizes):
    answer = 0
    tmp = 0
    first = []
    second = []
    
    for i in sizes:
        if i[0] < i[1]:
            tmp = i[0]
            i[0] = i[1]
            i[1] = tmp
    
    
    for i in range(len(sizes)):
        first.append(sizes[i][0])
        second.append(sizes[i][1])
        
    answer = max(first) * max(second)
    
    return answer