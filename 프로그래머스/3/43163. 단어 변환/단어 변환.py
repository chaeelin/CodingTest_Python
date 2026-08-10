from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = [False] * len(words)
    q = deque([(begin,0)])
    
    while q:
        word, step = q.popleft()
        
        if word == target:
            return step
        
        for i in range(len(words)):
            if visited[i]:
                continue
            
            count = 0
            
            for a,b in zip(word, words[i]):
                if a != b:
                    count += 1
                
            if count == 1:
                visited[i] = True
                q.append((words[i], step+1))
                    
    return 0