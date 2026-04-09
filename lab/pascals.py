def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
def ncr(n, r):
    return fact(n)//(fact(r)*fact(n-r))

def pascal(n):
    for i in range(n):
        for j in range(i+1):
            print(ncr(i, j), end=' ')
        print()
        
pascal(5)