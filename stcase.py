'''
read string from user and
swap cases
input: aBcD
output: AbCd'''
s=input("enter any string")
ns=""
for ch in s:
    if ch.islower()==True:
        ns=ns+ch.upper()
    else:
        ns=ns+ch.lower()
print(ns)
