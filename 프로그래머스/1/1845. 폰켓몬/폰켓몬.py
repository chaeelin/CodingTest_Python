def solution(nums):
    answer = 0
    pick = int(len(nums)/2)
    count = 0
    nums = set(nums)
    
    if len(nums) < pick:
        answer = int(len(nums))
    else:
        for i in range(1, len(nums)+1):
            count += 1
            
            if count == pick:
                answer = pick

    return answer