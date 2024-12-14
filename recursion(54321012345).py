def fun(n):
    if n==0:
        print(0)
        return 0
    print(n)
    fun(n-1)
    if n!=1:
        print(n)

x=int(input("enter the no:"))
fun(x)



