def solution(seoul):
    answer = '김서방은 '
    num = 0
    
    for i in seoul:
        if i == "Kim":
            num = seoul.index(i)
            
    return answer + str(num) + "에 있다"