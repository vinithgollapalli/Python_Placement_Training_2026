n = int(input())
count=0
sum=0
t=n
while n>0:
    n=n//10
    count+=1
n=t
while n>0:
    r=n%10
    n=n//10
    sum=sum+pow(r,count)
if sum==t:
    print("Armstrong number")
else:
    print("Not an Armstrong number")