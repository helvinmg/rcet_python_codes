#For loop with range
'''range(start,stop,step)
range(7) -> stop=7, start=0
range(2,10) -> stop=10, start=2
it will take upto stop-1, stop is excluded
step is by default +1
'''
for i in range(7):
    print(i)#0,1,2,3,4,5,6
for i in range(10,100):
    print(i)#10,11,12......99
for i in range(100,50):
    print(i)#no output due to invalid range
for i in range(100,50,-1):
    print(i)#100,99,98,97 ..... 51
for i in range(5,51,5):
    print(i)
