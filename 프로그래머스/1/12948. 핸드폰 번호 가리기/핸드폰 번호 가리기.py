def solution(phone_number):
    answer = ''
    
    s = phone_number[:len(phone_number)-4]
    for i in s:
        s = s.replace(i,"*")

    answer += s
    answer += phone_number[len(phone_number)-4:]
    
    return answer