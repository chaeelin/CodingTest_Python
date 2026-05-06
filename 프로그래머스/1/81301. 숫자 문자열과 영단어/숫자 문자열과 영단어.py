def solution(s):
    num = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    
    temp = ''
    answer = ""
    
    for i in s:
        temp += i
        
        if temp in num.keys():
            answer += num[temp]
            temp = ''
            
        elif i.isdigit():
            answer += i
            temp = ''

    return int(answer)