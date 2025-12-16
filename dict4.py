#built-in function of dict
stud1={'rahul':36,'anna':67,'sachin':55}
stud2={'manisha':45,'sachin':59,'anu':49}
stud1.update(stud2)
#dict1.update(dict2) -> dict2 items will be added to dict1
#if same key present in dict2 - updation will happen
print("after update: ",stud1)
#{'rahul':36,'anna':67,'manisha':45,'sachin':59,'anu':49}
#dict.pop(key) -> removes the pair with specified key
stud1.pop('rahul')#del stud1['rahul']
print("after pop: ",stud1)
stud1.popitem()#removes the last inserted pair
print("after popitem: ",stud1)
stud1.clear()
print("after clear: ",stud1)
