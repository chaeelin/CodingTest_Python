def solution(answers):
    answer = []
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    scores = [0,0,0]
    
    for i,ans in enumerate(answers):
        for student, pattern in enumerate(patterns):
            if ans == pattern[i%len(pattern)]:
                scores[student] += 1
    
    max_score = max(scores)
    
    for i in range(len(scores)):
        if max_score == scores[i]:
            answer.append(i+1)
    return answer