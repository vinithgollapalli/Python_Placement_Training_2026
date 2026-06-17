n=18
sum=0
for i in range(1,2):
    r=n%10
sum+=r
if sum%n==n:
    print("It is harshad number")
else:
    print("It is not harshad number")