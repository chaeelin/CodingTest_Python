def solution(array, commands):
    answer = []
    list = []
    
    for i in range(len(commands)):
        start = commands[i][0]
        finish = commands[i][1]
        cut = commands[i][2]
        list = sorted(array[start-1:finish])
        answer.append(list[cut-1])
        
    return answer