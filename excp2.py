try:
    d={}
    #print(d['a'])
    print(5/0)
except KeyError:
    print("Key error occured")
except Exception as e:
    print("This is the exception happened:",e)
finally:
    print("finally block")
