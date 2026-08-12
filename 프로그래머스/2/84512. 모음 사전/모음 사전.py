def solution(word):
    count = 0
    answer = 0
    
    def dfs(alpa): 
        nonlocal count, answer
        
        if alpa == word:
            answer = count 
            return count
        
        if len(alpa) > 5:
            return 
        
        count += 1
        
        for i in "AEIOU":
            dfs(alpa + i)

    dfs("")
    
    return answer