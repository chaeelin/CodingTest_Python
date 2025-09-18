import itertools
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.sqrt(n)) + 1  
    for i in range(3, limit, 2):  
        if n % i == 0:  
            return False
    
    return True

def solution(nums):
    answer = 0
    
    for comb in itertools.combinations(nums, 3):
        if is_prime(sum(comb)):
            answer += 1
    return answer