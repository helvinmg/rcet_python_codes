'''
0 1   2   3   4  5  6  7  8 9 10
a  b  c   d  e   f   g   h  i    j   k
-11                   -5  -4 -3 -2 -1
'''
#reverse index / negative index
st="abcdefghijklmn"
#-1 index will always give last element
print(st[-1])#n
print(st[-2])#m
print(st[-11])#d
print(st[-len(st)])#st[-14] -> first character
