#read a limit from user and print sum of even number till that limit
'''
input -10
output - 2+4+6+8+10=30
'''
limit=int(input("Enter the the limit:"))
evesum=0
for num in range(2,limit+1,2):
    evesum=evesum+num
print("Sum of even numbers:",evesum)

evesum=0
num=2
while num<limit+1:
    evesum=evesum+num
    num=num+2
print("Sum of even numbers:",evesum)
