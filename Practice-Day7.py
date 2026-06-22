#List Comprehension
# n=input("Enter name:")
# a=[i for i in  n if i not in "AEIOUaeiou"]
# print(a)

#Sort names based on no of char
#wap to create a shoping cart for a uper market like Dmrt and billgeneration
dic={"ThumbsUp":20,"Sprit":25,"Limka":30,"Maza":40}
dic_selected={}
quty=[]
print("Items:")
for i,_ in dic.items():
    print("*",i)
def buy():
    global items
    items=input("Enter items to buy :")
    global qut
    qut=int(input("Enter the quantity :"))
    dic_selected[items]=qut
    return items,qut
buy()
c=input("Do you want to buy (y|n)")
while c == 'y':
    buy()
    c=input("Do you want to buy (y|n)")
print("Your cart")
for i in range(len(dic_selected)):
    print(dic_selected[i],quty[i])