from collections import Counter

def solution(participant, completion):
    answer = ''
    
    answer = Counter(participant) - Counter(completion)
    answer = "".join(answer.keys())
    
    return answer