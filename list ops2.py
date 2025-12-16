#List Operations
marks=[34,56,77,25,50]
#add multiple values
#list.extend(anotherlist)
marks.extend([56,77,18])
print("after extend",marks)
#adding values anywhere
#list.insert(index,value)
marks.insert(1,50)
print("after insert",marks)
#delete by value - list.remove(value)
marks.remove(77)
print("after remove",marks)
marks.clear()
print("after clear",marks)
