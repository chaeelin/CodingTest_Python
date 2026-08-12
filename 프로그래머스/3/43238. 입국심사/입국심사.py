def solution(n, times):
    answer = 0
    
    left, right = 1, min(times) * n
    
    while left <= right: 
        mid = ((left + right) // 2)
        people = sum(mid // t for t in times)
        
        if people < n:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
    
    return answer