books=[]
while True:
    print("!---ELibary---!")
    print("1.addbooks\n2:ShowBooks\n3:UpdateBook\n4:DeleteBook\n5:Exit")
    choice=int(input("enter Choice number: "))
    if choice==1:
        title=input("Enter Book title").capitalize()
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
        if len(books)>0:
            old_book_title=input("Enter book title to update").capitalize()
            if old_book_title in books:
                new_title=input("Enter new title od book to update.").capitalize()
                books[books.index(old_book_title)]=new_title.capitalize()
                print(f"{old_book_title}book title updated succesfully")
            else:
                print(f"{old_book_title} book tile is not found try again")    
        else:
            print("no book available so first addd to book !!")        
    elif choice==4:
        if len(books)>0:
            old_book_title=input("Enter book title to remove").capitalize()
            if old_book_title in books:
                
                books.remove(old_book_title.capitalize())
                print(f"{old_book_title}Books removed succesfully")
            else:
                print(f"{old_book_title} book tile is not found try again")    
        else:
            print("no book available so first addd to book !!")   
    
    elif choice==5:
        print("Thanks for using our servies !!")
        break
