n=int(input("Enter the num:"))
even,odd=0,0
while(n):
    d=n%10
    if(d%2==0):
        even+=1
    else:
        odd+=1
    n=n//10
print("Even no count=",even)
print("Odd no count=",odd)