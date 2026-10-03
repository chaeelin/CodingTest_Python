def solution(brown, yellow):
    answer = []
    total = brown + yellow
    result = []

    
    for i in range(1, total + 1):
        if total % i == 0 and i<= total // i:
            result.append((i, total // i))

    for a,b in result:
        if (a-2) * (b-2) == yellow:
            answer.extend([b,a])

    return answer