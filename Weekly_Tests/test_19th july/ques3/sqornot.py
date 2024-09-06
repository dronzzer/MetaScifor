def squarecheck(x):
    for i in range(1,x//2 + 1):
        if i*i==x:
            i=True
            return True
    return False