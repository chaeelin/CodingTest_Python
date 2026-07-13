def solution(nums):
    num = len(nums) / 2
    
    nums = set(nums)
    
    if num > len(nums):
        return len(nums)
    else:
        return num