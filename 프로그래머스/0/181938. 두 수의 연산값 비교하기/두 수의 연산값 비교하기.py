def solution(a, b):
    if int(f"{a}{b}") >= int(f"{2*a*b}"):
        return int(f"{a}{b}")
    else:
        return int(f"{2*a*b}")