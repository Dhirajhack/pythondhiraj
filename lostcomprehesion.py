# # for i in range(1,11):
# #     print(i , end=" ")

# # list comperhesion
# #syntax [output for iterable_vairable in squence_object if condition]    

# # pint 1 to 10
# print([i  for i in range(1,11)])

# #print 1 to 10 number square 
# print([i*i  for i in range(1,11)])

# # print even number from 1 to 10
# for i in range(1,11):
#     if i%2==0:
#         print(i , end=" ")

# #print even nuber who divide by toooo        
# print([i  for i in range(1,11) if i%2==0])

# #wap to cerate  mylist add number as per count enter
# mylist=[]
# count=int(input("enter count to add number tilll"))
# for i in range(count):
#     number=int(input(f"enter number {i+1} =" ))
#     mylist.append(number)
# print(mylist)    


#  or use this 

# count=int(input("enter count to add number tilll"))

# mylist_new=[int(input("enter number")) for i in range(count)]
# print(mylist_new)

my_list=[1,4,2,67,246,600,2]
even=[]
old=[]
# for i in my_list:
#     if i%2==0:
#         even.append(i)
#     else:
#         old.append(i)    
# print(even)        

# or 

[even.append(i) if i%2==0 else old.append(i) for i in my_list]
print(old)
print(even)

