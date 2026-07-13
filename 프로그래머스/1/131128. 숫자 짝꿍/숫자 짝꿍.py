from collections import Counter

def solution(X, Y):
    answer = []
    
    X = Counter(X)
    Y = Counter(Y)
    
    for i in '9876543210':
        cnt = min(X[i], Y[i])
        answer.extend([i] * cnt)
        
    if not answer:
        return "-1"
    
    if answer[0] == '0':
        return "0"
    
    answer = "".join(answer)
    
    return answer