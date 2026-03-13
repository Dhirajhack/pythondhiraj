#dict:- collection of element represendted into key , value pair enclosed with {k:v}
#ot folloe key indeimg and key order slicing andit is mutable

#create empty dictionary
# d={}
# print(d,type(d))
# d1=dict()
# print(d1 , type(d1))

# d1={1:1000, 2:22000 , 3:2000 , 4:30000}
# print(d1)

# #student deatils
# d2={"rollnumber":101 , "name":"pooja" , "grade" : "a+"}
# print(d2)

# d3={"subjects" :["py" , "js" , "html " , "css"]}
# print(d3)


# d4={(1,2,3) :[1,4,9]}
# print(d4)

# d5={(1,2,3) :"rahul"}
# print(d5)
# #no operstion no sclicing
# #key index
# print(d2["name"])
# print(d3["subjects"])

# print(len(d3))
# print(len(d2))

#CRUD operation on emty dict withoput using method

books={}
print(books)
books["isbn"]=1111
print(books)
books["Isbn"]=5555 # update the  cuurent value o0f lat timnewe right
print(books)

books["title"]="python"
books["author"]="rossom"
books["pricxe"]=899
print(books)
books["dob" , "qty"]="12-04-2005" , 200
print(books)

#chnage ptice to
books["pricxe"]=12999
print(books)

#read the books title and price
print(books["title"] , books["pricxe"])

#delete author
del books["author"]
print(books)









