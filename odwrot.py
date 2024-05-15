def odwrot(array):
    if len(array)==1:
        return array
    else:
        s=array[0]
        t=odwrot(array[1:])
        return t+[s]
      
        
lis=[1,2,3,4,5,44362,111,1]
print(odwrot(lis))
