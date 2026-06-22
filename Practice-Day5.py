#Given a name and The index number of alphabet should be the nexxt alphabet
# def ev_ch(name):
#     for i in range(len(name)):
#         if i%2==0 and name[i].isalpha():
#             if name[i]=='z':
#                 print("a")
#             elif name[i]=='z':
#                 print("A")
#             else:
#                 print(chr(ord(name[i])+1),end=' ')
#         else:
#             print(name[i],end=' ')
# name=input("Enter a name:")
# ev_ch(name)

#Move Zeroes to Left or Right side pf the List
# def move_zeroes():
#     li=[1,1,0,25,0,1,0,6]
#     nz=[]
#     z=[]
#     for i in li:
#         if i == 0:
#             z.append(i)
#         else:
#             nz.append(i)
#     nz.extend(z)
#     print(nz)
# move_zeroes()


#To seperate list of values in given List as per their DT
# l=[2,4,5,3,6,"hi","Mom","Dad",True, False]
# li=[]
# ls=[]
# lb=[]
# for el in l:
#     if type(el) == int and el%2!=0:
#         li.append(el)
#     elif type(el) == str and el == el[::-1]:
#         ls.append(el)
#     elif type(el) == bool and el==True:
#         lb.append(el)
# print(li,ls,lb)

#Finding a next greatest number of a entered number in a list
l=[-2,56,41,21,2,56,98,32,678,69,415,4,641,5,12,3,2,8,69,524,7,65,2263]
n=int(input("Enter a number:"))
for i in range(n+1,max(l)+1):
    if i in l:
        print(i)
        break
else:
    print(f"{n} itself Greatest number")