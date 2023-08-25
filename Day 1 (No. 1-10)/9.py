def pytriplet():
    target_sum= 1000
    for a in range(1, target_sum // 2):
        for b in range(a, target_sum // 2):
            c = target_sum - a - b
            if a**2 + b**2 == c**2:
                return a, b, c, a*b*c

print(pytriplet())