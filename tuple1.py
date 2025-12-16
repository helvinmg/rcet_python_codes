#sequence values enclosed in paranthesis saparated by commas
#they are immutable
T1=tuple()
T2=()
print(T1, type(T1))
print(T2, type(T2))
T3=(1,2,3,"abc",2,2,1,5)
print(T3)
#access
print("1st ele: ",T3[0])
print("last ele: ",T3[-1])
print("slice: ",T3[:2])
print("no. of ele: ",len(T3))
#you can not perform any modification
#T3[0]=10
#del T3[0]
print("index of abc",T3.index("abc"))
print("count of 2: ",T3.count(2))
#both index and count same as in list
