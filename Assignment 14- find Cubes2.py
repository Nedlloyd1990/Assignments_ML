# assignment 14
cubes2_even=[]
list2=[2,3,5,8,12,16,27,32,64,216]

max_num=max(list2)
for i2 in range(1,max_num+1):
    value3=i2**3
    value4=i2%2
    if value3 in list2 and value4==0 :
        cubes2_even.append(value3)
        


print('The Cubes and even from the list are {}'.format(cubes2_even))
