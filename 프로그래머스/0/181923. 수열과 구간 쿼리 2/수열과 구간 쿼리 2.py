def solution(arr, queries):
    answer = []

    for s, e, k in queries:
        data = [] 
        for i in range(s, e + 1):  
            if arr[i] > k:
                data.append(arr[i])
        if data:
            answer.append(min(data))
        else:
            answer.append(-1)

    return answer
