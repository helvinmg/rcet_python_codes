vehicles=['cycle','bike','car','SUV','Bus','Boat']
#convert given list to a dictionary
#index as key and elements as value
#{0:'cycle',1:'bike',2:'car'..}
vehicle_dict={}
for i in range(0,len(vehicles)):
    vehicle_dict[i]=vehicles[i] 
    #print("index: ",i)
    #print("element: ",vehicles[i])
print("converted dict",vehicle_dict)
#index as value and elements as key
#{'cycle':0,'bike':1.....}
