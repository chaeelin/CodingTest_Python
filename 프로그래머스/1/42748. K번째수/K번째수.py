def solution(array, commands):
    answer = []
    i = 0
    j = 0
    j = 0
    
    for num in range(len(commands)):
        i = commands[num][0]
        j = commands[num][1]
        k = commands[num][2]
        a = array[i-1:j]
        a = sorted(a)
        a = a[k-1]
        answer.append(a)
        i = 0
        k = 0
    return answer
