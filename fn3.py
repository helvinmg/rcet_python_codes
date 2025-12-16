'''
create a function pow(m,n)
which display m raises to n
if n is not given it should
display square by default
if m is not given then it should
display a message to user stating
operation not possible

pow(5) -> 25
pow(5,3) -> 125
pow() -> "Operation Not Possible"'''

def pow(m=0,n=2):
    if m==0:
        print("not possible")
    else:
        print(m**n)

pow(5,3)
pow(5)
pow()

