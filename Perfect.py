# n=8128
# i=1
# sum=0
# while i<=n//2:
#     if n%i==0:
#         sum+=i
#     i+=1
# if sum==n:
#     print("Perfect number")
# else:
#     print("Not a perfect number")



n=int(input("Enter the number"))
i=1
count1=0
count2=0
sum=0
while(i<=n//2):
    if n%i==0:
        sum+=i
        count1+=1
    count2+=1
    i+=1
print("IF count",count1)
print("While count",count2)
if sum==n:
    print("perfect number")
else:
    print("Not a perfect number")