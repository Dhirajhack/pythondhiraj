students=[["id" , "name" , "grade"] , [1,"Ravi" , "o"] , [2,"mistest" , "a+"]]
# print(students)
# print(students[0])
# print(students[1])
# print(students[2])

# for i in students:
#     print(i)

# # find studnet name  and rande whoes id is 2
# print("studnt id 2 name is=" , students[2][1])
# print("studnt id 2 name is=" , students[2][2])

#Find student name and grade by entering student id 
id=int(input("enter if to find nam  and grade ="))
flag=False
for i in students:
    if i[0]==id:
        flag=True
        print("id=" , i[0])
        print("name" , i[1])
        print("grade" , i[2])
if flag==False:
    print("id  not found . try again !!")    

    