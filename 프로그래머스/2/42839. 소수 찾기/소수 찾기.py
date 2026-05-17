from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    count = 0
    put = []
    
    for i in numbers:
        count += 1
        result = list(permutations(numbers, count))
        
        for i in result:
            put.append(int("".join(i)))
        
    put = set(put)
        
    for i in put:
        if is_prime(int(i)):
            answer += 1
        
    return answer