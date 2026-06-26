from itertools import permutations

def solution(k, dungeons):
    answer = 0
    result = []
    kk = 0
    
    for perm in permutations(dungeons):
        kk = k
        answer = 0
        for dungeon in perm:
            if (kk >= dungeon[0]):
                kk = kk - dungeon[1]
                answer += 1
        result.append(answer)
        
    return max(result)