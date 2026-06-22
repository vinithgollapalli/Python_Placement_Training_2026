#Sample program for Class and Object
# class SRU:
#     def addmission(self):
#         print("Addmission Successfull")
#         print(self)
# sai=SRU()
# vinith=SRU()
# sai.addmission()
# vinith.addmission()



#Number guessing
def num_guess():
    import random
    num= random.randint(1,5)
    ch=5
    points=0
    while ch>0:
        g_num=int(input("ENter number to guess"))
        if ch == 5 and g_num == num:
            points +=10
            break
        elif ch == 4 and g_num == num:
            points +=8
            break
        elif ch == 3 and g_num == num:
            points +=5
            break
        elif ch == 2 and g_num == num:
            points +=3
            break
        elif ch == 1 and g_num == num:
            points +=1
            break
        else:
            ch-=1
    else:
        print(num)
try:
    num_guess()
except:
    print("Enter only nums")

#Read num from user and sum the num till it become single num then print th chr of position a-k
