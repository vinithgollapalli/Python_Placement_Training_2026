# #Greater and Lesser Age
# # ages=[]
# # for i in range(5):
# #     age=int(input("Enetr age:"))
# #     ages.append(age)
# # elr=ages[0]
# # you=ages[0]
# # for age in ages:
# #     if age>elr:
# #         elr=age
# #     if age<you:
# #         you=age
# # print(elr,you)



# #Even and Odd using Lists
# # even=[]
# # odd=[]
# # nums=list(map(int,input("Enter numbers:").split()))
# # for i in nums:
# #     if i%2==0:
# #         even.append(i)
# #     else:
# #         odd.append(i)
# # print(even,odd)



# #Names seperate Vowels and Consonants
# names=input("Enter names: ").split(",")
# vow="AEIOUaeiou"
# for name in names:
#     vc=" "
#     cc=" "
#     for ch in name:
#         if ch in vow:
#             vc+=ch
#         else:
#             cc+=ch
#     print(name)
#     print("VOwels are:",vc,"Consonants are:",cc)
#     print("____________________________")



#Suggesting a new name from FN and LN
# names=input("Enter names:").split(",")
# if len(names)==2:
#     if names[0].isalpha() and names[1].isalpha():
#         if len(names[0])>=2 and len(names[1])>=2:
#             nick=names[0][-2:]+names[1][0:2]
#             print(nick[::-1])
#         else:
#             print("Name should contain min 2 characters")
#     else:
#         print("Only alphas are allowed")
# else:
#     print("Only 2 names are allowed ")



#Count of similar adjacents
# l=[1,2,2,3,4,4,1]
# c=0
# for i in range(len(l)):
#     if l[i]==l[i-1]:
#         c+=1
# print(c)


#Giving Lucky names with names
vowels="AEIOUaeiou"
names=input("Enter a name:").split(",")
if names[0][-1] in vowels:
        print("Lucky name ")
else:
    print("Not Lucky name")
    