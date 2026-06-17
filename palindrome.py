n=int(input("Enter a number: "))
sum=0
t=n
while n>0:
    r=n%10
    n=n//10
    sum=sum*10+r
if t==sum:
    print("Palindrome number") 
else:
    print("Not a palindrome number")