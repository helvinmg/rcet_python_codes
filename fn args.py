#special argument
def add(a,b,*nums):
    print("a=",a)
    print("b=",b)
    print("nums=",nums)
    print(a+b+sum(nums))

add(6,7)
add(2,3,4,5,6,7,8,9)
#keyword args
def disp(**info):
    print("info=",info)

disp(name="srk",age=55)
