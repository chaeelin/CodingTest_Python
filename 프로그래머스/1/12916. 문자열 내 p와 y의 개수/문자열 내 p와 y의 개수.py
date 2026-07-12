def solution(s):
    answer = True
    county = 0
    countp = 0
    
    for i in s:
        if i == "y" or i == "Y":
            county +=1
        if i == "p" or i == "P":
            countp +=1
    
    if county != countp:
        return False

    return True