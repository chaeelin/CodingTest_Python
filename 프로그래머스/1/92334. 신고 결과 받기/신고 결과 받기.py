from collections import defaultdict

def solution(id_list, report, k):    
    reported = defaultdict(set)
    
    for i in set(report):
        a, b = i.split()
        reported[b].add(a)
    
    result = {uid: 0 for uid in id_list}
    
    for target,sender in reported.items():
        if len(sender) >= k:
            for s in sender:
                result[s] += 1
    
    return [result[uid] for uid in id_list]