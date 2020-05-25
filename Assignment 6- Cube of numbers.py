def cube(x):
    cube_i=0
    for i in str(x):
        z=int(i)**3
        cube_i=z+cube_i
    if cube_i==x:    
        print('{} is an Armstrong number'.format(x))
    else:
        print('{} is not an Armstrong number'.format(x))
        
cube(371)    