def solution(n):
    answer = 0
    if n % 2 != 0:
        for i in range(n+1):
            if i % 2 != 0:
                answer = answer + i
        return answer
    else:
        for i in range(n+1):
            if i % 2 == 0:
                answer = answer + pow(i,2)
        return answer
                