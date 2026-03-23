def solution(answers):
    answer = []
    a = b = c = 0
    
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == first[i % len(first)]:
            a += 1
        if answers[i] == second[i % len(second)]:
            b += 1
        if answers[i] == third[i % len(third)]:
            c += 1

    if max(a,b,c) == a:
        answer.append(1)
        
    if max(a,b,c) == b:
        answer.append(2)
        
    if max(a,b,c) == c:
        answer.append(3)

    return answer