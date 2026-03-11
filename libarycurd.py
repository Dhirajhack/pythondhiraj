books=[]
while True:
    print("!---ELibary---!")
    print("1.addbooks\n2:ShowBooks\n3:UpdateBook\n4:DeleteBook\n5:Exit")
    choice=int(input("enter Choice number: "))
    if choice==1:
        title=input("Enter Book title").lower()
        if title not in books:

            books.append(title)
            print("Books added succefully")
        else : 
            print(f"{title} Book is already exists so add another book !!")   
    elif choice==2:
        if len(books)==0:
            print("no book avalibale try again")
        else:
            print("avaliable books are" , books)    
    elif choice==3:
        pass
    elif choice==4:
        pass
    elif choice==5:
        print("Thanks for using our servies !!")
        break
