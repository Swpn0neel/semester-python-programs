def lprimefact(n):
    lpf= 0
    for i in range(1, n+1):
        if n%i==0:
            c=0
            for j in range(1, i):
                if i%j==0:
                    c=c+1
            if c==1:
                lpf= i
    return lpf