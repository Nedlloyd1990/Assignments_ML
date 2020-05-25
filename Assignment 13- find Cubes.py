# assignment 13
cubes1=[]

max_num=max(list2)
for i2 in range(1,max_num+1):
    value3=i2**3
    if value3 in list2:
        cubes1.append(value3)
        
list2=[2,3,5,8,12,16,27,32]
print('The Cubes from the list are {}'.format(cubes1))