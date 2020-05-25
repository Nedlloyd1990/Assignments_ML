value=341
x=[]
count=1
counter=0
new_value=0
x1=[]

for loop in range(value):
    if counter==0 and new_value <9 :
        for i in str(value):
            x.append(int(i))
        for mult in x:
            count=count*mult
        x1.append(count)
        new_value=count
        count=1
        counter=counter+1
        x.clear()         
    elif counter>0 and new_value>9 :
        for i in str(new_value):
            x.append(int(i))  
        for mult in x:
            count=count*mult
        x1.append(count)            
        new_value=count
        count=1
        counter=counter+1
        x.clear()
        
print('MDR is  for value {} is {}'.format(value,new_value))  
