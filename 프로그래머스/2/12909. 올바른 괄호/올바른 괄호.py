from collections import deque

def solution(s):
    answer = True
    q = deque(s)
    stack = []
    
    for i in q:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                stack.pop()
                
    if stack:
        return False

    return True