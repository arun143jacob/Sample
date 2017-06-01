def product(a):
    s = 1;
    for i in a:
        s = s * i;
    print s

    
def factorial(n):
    f = product(list(range(1, n+1)))
    
factorial(6)