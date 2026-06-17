n=int(input("Enter a number:"))
sum=0
t=n
while n>0:
    r=n%10
    n=n//10
    fact=1
    while r>1:
        fact= fact*(r*(r-1))
        r-=2
    sum+=fact
if t==sum:
    print("Strong number")
else:
    print("Not a strong number")
    
