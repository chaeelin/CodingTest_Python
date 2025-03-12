def solution(ineq, eq, n, m):
    if eq == "!":
        if eval(f"{n}{ineq}{m}") == 1:
            return 1
        else:
            return 0
    else:
        if eval(f"{n}{ineq}{eq}{m}") == 1:
            return 1
        else:
            return 0
        
        