def solution(num_list):
    answer = []
    list = sorted(num_list)
    for i in range(5):
        answer.append(list[i])
    return answer