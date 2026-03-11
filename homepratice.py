# left  traingle
# count=5
# for  i in range(count):
#     for j in range(i):
#         print("*" , end="")
#     print()    

# # upper reversed trigale
# count=5
# for  i in range(count , 0 , -1):
#     for j in range(i):
#         print("*" , end="")
#     print()    


# count=5
# for  i in range(1 , count+1):
#     for j in range(count - 1):
#         print(" " , end="")

#     for k in range(i):
#         print("*" , end="")
#     print()    

count = 5

for i in range(1, count + 1):
    for j in range(count - i):
        print (" " ,end=""),
    for k in range(i):
        print ("*" ),
    print