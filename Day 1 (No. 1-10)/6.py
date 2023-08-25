def sum_square_difference(n):
    s, s1= 0, 0
    for i in range(1, n+1):
        s= s+i
        s1= s1+ (i**2)
    s= s**2
    diff= s - s1
    return s1, s, diff

print(sum_square_difference(10))