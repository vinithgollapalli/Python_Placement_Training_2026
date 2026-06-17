n=9
sum=0
res=n**2
while(res>0):
    r=res%10
    res=res//10
    sum=sum+r
if(n==sum):
    print("Neon Number")
else:
    print("Not a neon number")