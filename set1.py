#set is mutable
#set is unordered - there is no index
#set won't have duplicate values
S1={}#this will be empty dict
S2=set()
print(S1,type(S1))
print(S2,type(S2))
users={"rahul","manu","varun"}
print(users)
users.add("geeta")
print("after addition",users)
users.remove("rahul")
print("after removal",users)
#pop() will remove a random value
#users.clear()#to empty the set
#print("after clear",users)
#print(users[0])#error
marks={25,33,45,25,29,33}
print(marks)#it will have only unique


