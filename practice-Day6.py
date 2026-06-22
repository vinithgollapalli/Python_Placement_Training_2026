#Twin Prime Check
# def is_prime(n):
#     for i in range(2,n):
#         if n%i ==0:
#             return False
#     else:
#         return True
# try:
#     n=int(input("ENter a number:"))
#     if is_prime(n) and is_prime(n+2) or is_prime(n-2):
#         print("Twin Prime")
#     else:
#         print("Get Lost !!!")
# except:
#     print("Only Ints")

#Recursion for given number
# def factorial(n):
#     if n<=1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(6))

#caluculate time taken by program adding 2 numbers
# import time
# st=time.time()
# def add(n,m):
#     return n+m
# n=int(input("Enter a number:"))
# m=int(input("Enter b number:"))
# print(add(n,m))
# et=time.time()
# print(et-st)

#Vendor wants to carry as less he can take cans to give for customer
# req = int(input("Enter requirement: "))
# cans_in_liters = [10, 5, 2, 1]
# total_cans = 0
# for can in cans_in_liters:
#     count = req // can
#     total_cans += count
#     req %= can
# print("Minimum cans required:", total_cans)



