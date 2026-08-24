def solution(record):
    answer = []
    users = {}
    state = []
    
    for i in record:
        part = i.split()
        
        if part[0] == "Enter" or part[0] == "Change":
            uuid = part[1]
            name = part[2]
            users[uuid] = name
            
        state.append((part[0],part[1]))
        
    for i in state:
        if i[0] == "Enter":
            answer.append(users[i[1]] + "님이 들어왔습니다.")
        if i[0] == "Leave":
            answer.append(users[i[1]] + "님이 나갔습니다.")

    return answer