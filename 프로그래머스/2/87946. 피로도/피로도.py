def solution(k, dungeons):
    answer = -1
    visited = [False] * len(dungeons)
    result = []
    
    def dfs(number, count):
        nonlocal answer
        
        answer = max(answer, count)
        
        for i in range(len(dungeons)):
            if not visited[i] and number >= dungeons[i][0]:
                visited[i] = True
            
                numbers = number - dungeons[i][1]
            
                dfs(numbers, count + 1)
                
                result.append(count)
                visited[i] = False
            
    dfs(k,0)
    
    return answer