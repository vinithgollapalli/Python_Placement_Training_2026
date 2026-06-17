x=int(input("Enter your age: "))
if 0<x<=100:
    print("Enter your correct age:")
    x=int(input())
    if 0<x and x<=13:
        print("You belong to child category")
    if 14<=x and x<=18:
        print("You belong to teen category")
    if 19<=x and x<=30:
        print("You belong to young category")
    if 31<=x and x<=50:
        print("You belong to adult category")
    if 51<=x and x<=100:
        print("You belong to old category")