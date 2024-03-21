def factR(n):
    if n==1 or n==0:
        return 1
    return n*factR(n-1)

print(factR(5))