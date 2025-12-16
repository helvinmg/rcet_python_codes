limit=int(input("Enter the the limit:"))
evesum=0
for num in range(2,limit+1,2):
    evesum=evesum+num
print("Sum of even numbers:",evesum)
oddsum=0
for num in range(1,limit+1,2):
    oddsum=oddsum+num
print("Sum of odd numbers:",oddsum)
#using singe loop
evesum=oddsum=0
for num in range(1,limit+1):
    if num%2==0:
        evesum=evesum+num
    else:
        oddsum=oddsum+num
print("Sum of even numbers:",evesum,"Sum of odd numbers:",oddsum)
