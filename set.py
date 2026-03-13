# j=1
# while j<=10:
#     if j==5:
#         j+=1
#         pass
#     else:
#         print(j)
#         j+=1
# print("while outside")

#add elements
x={6,89,45,34,90}
print(x)
# print(x[-1]) # no inde follows
x.add(100) #add new element in anywhere
print(x)
x.add(90) #dont add but  n error because set allows because set sows without reperst
print(x)

# x.add(11,22) #TypeError: set.add() takes exactly one argument (2 given)
x.add((11,12))
print(x)
y={1,2}
x.update(y)
print(x)

colors={"red" , "green" , "pink" , "orange"}
print(colors)
colors_new=list(colors)
print(colors_new)
i=colors_new.index("red")
colors_new[i]="light red"
print(colors_new)
colors_new1=set(colors_new)
print(colors_new1)


#wap to show give unifue eleents from below given list
mylist=[12,12,45,23,75,78,45,1,1,1]
print(mylist)
new_list=list(set(mylist))
print(new_list)

# or this 
# new_mylist=[]
# for i in mylist:
#     if i not in  new_mylist:
#         new_mylist.append(i)

# print(new_mylist)

#WAP to create my set anf add number element as enters count
# mycount=set()
# print(mycount,type(mycount))
# count=int(input("enter count you want to enter"))
# for i in range(count):
#     numberlist=int(input(" enter number "))
#     mycount.add(numberlist)
# print(mycount)    
# count=int(input("enter count you want to enter"))
# myset1=({int(input(" enter number ")) for i in range(count)})
# print(myset1)


# print({i for i in range(-10 , 1 )})








# x={12,-324,56,343,-5,35}
# #Wap to show only  +ve number from above use comperhension
# print({i  for i in x if i>0})

# WAP to show sum of element of below list
mylist=[12,3,4,5,11]
# print=([ i for i in mylist if i>0 sum=+sum])
sum=0
for i in mylist:
    
        sum+=i
        
print(sum)        

# print(sum(mylist))

#Wao to show cube of above elements
for i in mylist:
        sum*=i
print(sum) 

print([i**3 for i in mylist])





