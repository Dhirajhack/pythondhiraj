#metho-count  , finf , replace , join , index , split , splitline ,z fill

#iterate string
name="ITvedant"
# for i in name:
#     print(i)

# #strinng in revers
# print("reverse string :" , name[::-1])

# for i in name :
#     print("reverse string :" , name[::-1])

# new="".join(reversed(name))
# print(new)

# newstr=""
# for i in name:
#     newstr=i+newstr
# print(newstr)    

# withoutvowel_str=""
# for i in name:
#     if i not in "aeiouAEIOU":
#         withoutvowel_str=withoutvowel_str+i
# print(withoutvowel_str)        

#WAP to print number of occurances of entered
#character from any string

# str=input("enter string=")
# char=input("enter characeter=")
# count=0

# for i in str:
#     if char==i:
#         count+=1
# print(f"{char} character count into {str} is {count}")        

str=input("enter string =")
chkstr=input(" enter char / worrd and show count=")
count=0
check=""
for i in range(len(str)):
    # print(i,str[i])
    k=i
    try:
        check+=str[k]
        k+=1
    except:
        None    
    if check==chkstr:
        count+=1
    check=""    

if count!=0:
    print(f"{chkstr} found {str} anf count={count}")    
else :
    print(f"{chkstr} not found in {str}")    
