def pali(n):
    return str(n) == str(n)[::-1]

def lpalipro():
    maxpali=0
    for i in range(100,1000):
        for j in range(i,1000):
            product= i*j
            if pali(product)==True and product>maxpali:
                maxpali= product
    return maxpali

print(lpalipro())