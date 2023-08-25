def sprime(n):
    s=0
    for i in range(2, n):
        c=0
        for j in range(1, i):
            if i%j==0:
                c+=1
        if c==1:
            s+= i
    return s