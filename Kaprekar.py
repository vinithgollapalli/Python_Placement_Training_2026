n=9
sum=0
res=n**2
r=res%pow(10,1)
l=res//pow(10,1)
sum=r+l
if(sum==n):
    print("It is Kaprekar number")
else:
    print("It is not Kaprikar number")
