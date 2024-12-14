def fun(n):
    if n==0:
        return 200
    print(n)
    t=fun(n-1)
    return t
x=5
print(fun(x))


