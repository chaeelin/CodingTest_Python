def solution(nums):
    pick = len(nums) / int(2)
    
    set_nums = set(nums)
    list_nums = list(set_nums)
    
    if len(list_nums) <= pick:
        return len(list_nums)
    else:
        return pick
