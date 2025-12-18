#for with else
for i in range(10):
    print(i)
    if i==5:
        break
else:
    print("loop completed")
#application in search
search="qwe"
users=["abc","xyz","pqr"]
for user in users:
    if search==user:
        print("found")
        break
else:
    print("not found")
    
