# # Function Caluculator
# # def add(n1,n2):
# #     print(n1+n2)
# # def sub(n1,n2):
# #     print(n1-n2)
# # def mul(n1,n2):
# #     print(n1*n2)
# # def div(n1,n2):
# #     print(n1/n2)
# # n1=int(input("ENter first num:"))
# # op=input("Select\n1.add\n2.sub\n3.mul\n4.div")
# # n2=int(input("Enter another number:"))
# # if op =='1':
# #     add(n1,n2)
# # elif op == '2':
# #     sub(n1,n2)
# # elif op == '3':
# #     mul(n1,n2)
# # elif op == '4':
# #     div(n1,n2)




# #ICE-CREAm PARLOUR MENU and BILL GENERATION
# def bs():
#     am=50
#     qu=int(input("Enter Quantity"))
#     bill=am*qu
#     print("________________________________")
#     print("Amount:", bill)
#     print("GST: 18 rs")
#     print(bill+18)
#     print("________________________________")
# def van():
#     am=30
#     qu=int(input("Enter Quantity"))
#     bill=am*qu
#     print("________________________________")
#     print("Amount:", bill)
#     print("GST: 18 rs")
#     print(bill+18)
#     print("________________________________")
# def sb():
#     am=30
#     qu=int(input("Enter Quantity"))
#     bill=am*qu
#     print("________________________________")
#     print("Amount:", bill)
#     print("GST: 18 rs")
#     print(bill+18)
#     print("________________________________")
# def mwa():
#     am=120
#     qu=int(input("Enter Quantity"))
#     bill=am*qu
#     print("________________________________")
#     print("Amount:", bill)
#     print("GST: 18 rs")
#     print(bill+18)
#     print("________________________________")
# print("\t**Welcome to ICE-MAGIC")
# op=input("Menu\n1.BS---50/-\n2.VAN---30/-\n3.SB---30/-\n4.MWA---120/-")
# if op == '1':
#     bs()
# if op == '2':
#     van()
# if op == '3':
#     sb()
# if op == '4':
#     mwa()
# else:
#     print("*********Invalid Option*********")


#ATM WITHDRAWAL
# import time
# amount=30000
# def withdraw():
#     global amount
#     am=int(input("Enter amount to WIthdraw:"))
#     if am<= amount and am>0:
#         if am%100 ==0:
#             print("Withdraw Success")
#             amount= amount-am
#             time.sleep(5)
#             print("Thanks for using FBI")
#         else:
#             pass
#     else:
#         print("Invalid Amount")
# def deposit():
#     global amount                                   
#     am=int(input("Enter amount to Deposit:"))
#     if am>0:
#         if am%100 ==0:
#             print("Deposit Success")
#             amount= amount+am
#             time.sleep(5)
#             print("Thanks for using fraud bank")
#         else:
#             print("Enter only 100 multiples")
#     else:
#         print("Invalid Amount")
# def checkbalance():
#     print("Balance:",amount)
# def transfer():
#     global amount
#     ac=int(input("Enter the account number :"))
#     dac=int(input("Re_enter account number"))
#     if ac==dac:
#         am=int(input("enter the amount to Transfer :" ))
#         if am > 0:
#             print("Transfer Success")
#             time.sleep(5)
#             print("Thanks for using Fraud Bank")
#     else:
#         print("acount number not matching")
# print("\t\t**Welcome to FBI**")
# ch=3
# while ch>0:
#     name=input("Enter Username:")
#     psw=input("Enter password:")
#     if name=="admin" and psw=="22161":
#         print("Login Successfull")
#         op=input("Select\n1.Withdraw\n2.Deposit\n3.Check balance\n4.Transfer")
#         if op=='1':
#             withdraw()
#             break
#         elif op=='2':
#             deposit()
#             break
#         elif op=='3':
#             checkbalance()
#             break
#         elif op=='4':
#             transfer()
#             break
#         else:
#             print("Invalid")


#Sum of FH list and LH list is equal and prime
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
nums=list(map(int,input().split()))
mid=len(nums)//2
fh=sum(nums[:mid])
sh=sum(nums[mid:])
if fh==sh:
    isprime(fh)
    print("Pizza")
else:
    print("False")






