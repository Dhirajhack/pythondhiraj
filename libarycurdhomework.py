books=[]
while True:
    print("--- Books store ---")
    print("1.addbook\n2:show book \n3: update book \n4: delete book \n5 exist Store")
    choice=int(input("enter number to select  program"))
    if choice==1:
        title=input("enter title of book : ").capitalize()
        if title not in books:
            books.append(title)
            print(f"{title}book added successfully")
        else:
             print(f"{title} Book is already exists so add another book !!")  
    elif choice==2:
        if len(books)==0:
            print(" no books available")              
        else:
            print("this are books" , books)    
    elif choice==3:
        if len(books)>0:
            old_book_title=input("book name serach here")
            if old_book_title in books:
                new_books_title=input("enter new book title").capitalize()
                books[books.index(old_book_title)]=new_books_title.capitalize()
                print(f"{old_book_title} update to new succefulll")
            else:
                print(f"{old_book_title} book tile is not found try again")    

        else:
           print(f"{old_book_title} book tile is not found try again")   

    elif choice==4:
        pass
    elif choice==5:
        print("thanks to vist")
        break
