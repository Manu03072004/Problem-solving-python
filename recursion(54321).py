def fun(n):
    if n==0:
        return 0
    print(n)
    fun(n-1)
x=int(input("enter the no:"))
fun(x)

