def number(n):
    nstr= str(n)
    maxproduct= 0
    maxdigits= ""
    for i in  range(len(nstr)-12):
        adjdigits = nstr[i:i+13]
        p= 1
        for digit in adjdigits:
            p*= int(digit)
        if p > maxproduct:
            maxproduct = p
            maxdigits = adjdigits
    return maxproduct, int(maxdigits)