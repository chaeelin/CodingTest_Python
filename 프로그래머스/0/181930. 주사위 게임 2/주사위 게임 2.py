def solution(a, b, c):
    if a != b and b != c and a!=c:
        return a+b+c
    else:
        if a==b or a==c or b==c:
            if a!=c or a!=b :
                return (a+b+c)*(pow(a,2)+pow(b,2)+pow(c,2))
            else:
                return (a+b+c)*(pow(a,2)+pow(b,2)+pow(c,2))*(pow(a,3)+pow(b,3)+pow(c,3))