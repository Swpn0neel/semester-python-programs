def nprime(n):
    i, num= 1, 2
    while i<=n:
        c= 0
        for j in range(1,num):
            if num%j==0:
                c+=1
        if c==1:
            i+=1
            x=num
        num+=1
    return x