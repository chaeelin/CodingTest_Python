def solution(numLog):
    answer = '';
    for i in range(len(numLog)):
        if i == 0:
            continue
        elif numLog[i-1] + 1 == numLog[i]:
            answer += "w"
        elif numLog[i-1] == numLog[i] + 1:
            answer += "s"
        elif numLog[i-1] + 10 == numLog[i]:
            answer += "d"
        elif numLog[i-1] == numLog[i] + 10:
            answer += "a"
    return answer