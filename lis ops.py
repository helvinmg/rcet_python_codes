#Read a list from user and perform the following operations
#remove all multiples of 5
#reverse the list
#find sum of even numbers
lst=eval(input("Enter the values in list format: "))
print(lst)
#remove all multiples of 5
newlst=[]
for value in lst:
    if value%5!=0:
        newlst.append(value)
print("list without multiples of 5",newlst)
print("reverse of list",newlst[::-1])
sum=0
for value in newlst:
    if value%2==0:
        sum=sum+value
print("sum of even number",sum)

