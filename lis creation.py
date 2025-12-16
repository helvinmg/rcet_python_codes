'''
Create a numeric list by reading values from user
'''
num_list=[]
n=int(input("how many value you want to enter"))
for i in range(n):
    ele=int(input("Enter the value"))
    num_list.append(ele)
print("List created:",num_list)
num_list.sort()
print("Sorted List:",num_list)
