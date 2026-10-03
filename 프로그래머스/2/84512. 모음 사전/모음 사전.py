def solution(word):
    answer = 0
    count = 1
    
    def dfs(alpa):
        nonlocal count, answer
        
        words = ""
        
        for i in "AEIOU":
            words = alpa + i
            print(words)
            
            if words == word:
                answer = count
        
            if len(words) > 5:
                return
        
            count += 1
            
            dfs(words)
    
    dfs("")
            
    return answer