# count=int(input("enter numbero frow "))
# n=1
# for i in range(count):
#     for j in range(i+1):
#         print("*" , end="")
       
#     print()    


# count=int(input("enter numbero row "))

# for i in range(count):
#     for j in range(count , i , -1):
#         print("*" , end="")
       
#     print()  


# count=int(input("enter numbero row "))
# for i in range(count):
#     for j in range(i+1):
#         print("*" , end="")   
#     print()    

# Right incement pyramid

# count=int(input("enter number row "))
# for i in range(count):
#     for k in range(count , i , -1):
#         print(end=" ")   
#     for j in range(i+1):
#         print("*" , end="")

#     print()        


# tree method 
# count=int(input("enter number row "))
# for i in range(count):
#     for k in range(count , i , -1):
#         print(end=" ")   
#     for j in range(i+1):
#         print("* " , end="")

#     print()        

# right decrement pyramind
    
count=int(input("enter number row "))
for i in range(count):
    for k in range(i):
        print(end=" ")   
    for j in range(count , i , -1):
        print(" *" , end="")

    print()        
