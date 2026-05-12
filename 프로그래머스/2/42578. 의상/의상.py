def solution(clothes):
    answer = 1
    list = {}

    for i in range(len(clothes)):
        list[clothes[i][1]] = list.get(clothes[i][1], 0) + 1
    
    for v in list.values():
        answer *= (v + 1)
        
    return answer - 1