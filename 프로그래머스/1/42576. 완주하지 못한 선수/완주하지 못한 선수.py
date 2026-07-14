from collections import Counter

def solution(participant, completion):
    answer = ''
    
    answer = "".join(list(Counter(participant) - Counter(completion)))
    
    return answer