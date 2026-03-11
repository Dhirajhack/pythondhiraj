list1=[ 11,34,56,23,19 ]
print(list1)

# operation
x=[1,2]
y=[2,4,6]
print(x+y)
# print(x+190) shold be list
x.append(100)
print(x)

x[2]=222
print(x)
# x[7]=99
# print(x)


#methods
#add element into list append() , insert()

colors=[]
print(colors)
colors.append("red")
print(colors)
colors.append("green")
print(colors)
colors.append(["blue" , "yellow"])
print(colors)
print(colors[-1])
colors.append({"grey" , "black"})
print(colors)
colors.append({"briyani" , "murga"})
print(colors)
colors.append({"#ffffff":"mobile"})
print(colors)
#updatelast elememt
colors[-1]="maroon"
print(colors)

#add element by using insert
colors.insert(0,"orange")
print(colors)
print(len(colors))
colors.insert(1,"cream")
print(colors)
print(colors.index("cream"))

# delete element
colors.pop() # always delete form last 
print(colors)

colors.pop(2) # we can delete using index number
print(colors)

# colors.remove("red") we can remove with name
# print(colors)

del colors[0]
print(colors)

# traversing list
for i  in colors:
    print(i)