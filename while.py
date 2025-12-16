#printing characters using while loop
st=input("enter the string")
print("first loop")
i=0
while i<len(st):
    print(st[i])
    i+=1#i=i+1
    
print("second loop")
#print string characters in rev using while
i=len(st)-1
while i>=0:
    print(st[i])
    i-=1#i=i-1
