'''
Exception Handling
What is exception ? -  Run Time Erros
'''
try: 
    L=[2,3,4,5]
    print(L[3])
except Exception:
    print("Handling Exception")
finally:
    print("I always work")
    #free resources and memory
