#List Operations
marks=[34,56,77,25,50]
#access - index/slice
print(marks[0])
print(marks[2:5])
#update
marks[0]=35
print("after update",marks)
#adding values
#list.append(singlevalue)
marks.append(66)
print("after add",marks)
#deletion - list.pop(index)
marks.pop()
marks.pop(0)#del marks[0]
print("after pop",marks)
