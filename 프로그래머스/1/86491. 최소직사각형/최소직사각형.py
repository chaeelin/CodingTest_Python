def solution(sizes):
    answer = 0
    big = []
    small = []

    for i,j in sizes:
        big.append(max(i,j))
        small.append(min(i,j))
        answer = max(big) * max(small)
        
    return answer