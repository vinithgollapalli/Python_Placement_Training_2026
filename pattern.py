#Pyramid
# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print(" ")


#Mirror Pyramid
# for i in range(1, 5):
#     for j in range(4 - i):
#         print(" ", end=" ")
#     for k in range(i):
#         print("*", end=" ")
#     print()

#Pyramid and Mirror Pyramid
# n = 4
# for i in range(1, n + 1):
#     for j in range(i):
#         print("* ", end="")
#     for j in range(2 * (n - i)):
#         print("  ", end="")
#     for j in range(i):
#         print("* ", end="")
#     print()

#Square
# n=6
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#Alphabets Pyramid
# n=4
# ch=65
# for i in range(n):
#     for j in range(i+1):
#         print(chr(ch), end=" ")
#         ch+=1
#     print(" ")


#Diamond Pattern

row=5
for i in range(row):
    for j in range(row-i-1):
        print(" ", end=" ")
    for k in range(2*i+1):
        print("*", end=" ")
    print()
for i in range(row-2,-1,-1):
    for j in range(row-i-1):
        print(" ", end=" ")
    for k in range(2*i+1):
        print("*", end=" ")
    print()
