def solution(l, r):
    answer = []
    for i in range(l,r+1):
        i = str(i)
        valid = True
        
        for j in i:
            if j != '0' and j != '5':
                valid = False
                break
        if valid:
            i = int(i)
            answer.append(i)
            
    if answer == []:
        return [-1]
    return answer