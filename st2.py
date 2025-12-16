'''accept a string from user and create a new string by combining alternative characters
input - apple
output- ape'''
st=input("enter the string")#abcdefgh
stnew=""
for i in range(0,len(st),2):#0,8,2 -> 0,2,4,6
    stnew=stnew+st[i]
print(stnew)#aceg
