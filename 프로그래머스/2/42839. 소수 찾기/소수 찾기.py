from itertools import permutations

def solution(numbers):
    answer = 0
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
    nums = set()
    
    for r in range(1, len(numbers) + 1):
        for p in permutations(numbers, r):
            nums.add(int(''.join(p)))
            
    for i in nums:
        if is_prime(i) == True:
            answer += 1
            
    return answer