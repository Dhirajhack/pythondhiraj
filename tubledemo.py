# tuble collection difient enclosed into () parenthsis
# it is squrnece , index follows , orders is it immutable men cant crud to operation 

# creacte tuple

tup=()
print(tup , type(tup))
t1=tuple()
print(t1 , type(t1))
t2=(500)
print(t2 , type(t2))

t3=(500,100 , "hello" , True , 5j , 89 , 8789)
print(t3 , type(t3))

# t4=tuple(78,89,90)
# t4=tuple(78,89,90)
# print(t4 ,type(t4))
my_tuple=(3,45,64,74,84,100)
#index
print("first element=" , my_tuple[0])
print("last elemnet"  , my_tuple[-1])

#sclicing
print(my_tuple[::-1])
print(my_tuple[2:5])

#operation
tuple1=(1,2,3)
tuple2=(4,5,6)
print(tuple1+tuple2)
# print(tuple1+100) #typeerror : can concate tuple (not "int") to tuple


#tuple function
tuple3=(1,5,4,2,3)

print(sorted(tuple3))
print(sorted(tuple3)[::-1]) # reverse usingn sorrt and ::-1

print(sorted(tuple3,reverse=True))

#tuble method-index()
tuble4=("hello" , "red" , "orange" , "green " , 100 , 200 , 700 , 1000 , 1000)
# print(tuble4.index(3)) # if element not preseny thgen valueerror
print(tuble4.index(100))
print(tuble4.count(1000))

# #immutabilltiy
# tuble4[0]="welcome" # TypeError: 'tuple' object does not support item assignment
# print(tuble4)

#traverising of tuble
my_tup=(100,200,300,400,500,1,2,3,4)

#ascending
for i in sorted(my_tup):
    print(i)

#descending    

for i in sorted(my_tup)[::-1]:
    print(i)






