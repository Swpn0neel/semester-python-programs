def fibo():
    a, b, c, s= 0, 1, 0, 0
    while c<4000000:
        c= a+b
        if c%2==0:
            s+= c
        a=b
        b=c
    return(s)