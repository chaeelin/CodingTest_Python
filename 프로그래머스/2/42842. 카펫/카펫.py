def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            w = i + 2
            h = (yellow // i) + 2 
            if brown == w * h - (w-2) * (h-2):
                answer = [w, h]
                
    return answer