collect=[]

def sumPdivisors(x):   
    for i in range(1,x):
        i1=x%i
        if i1==0:
            collect.append(i)
    sum_all=sum(collect)    
    print('The sum of all proper divisors of {} is {}' .format(x,sum_all))
    
    
sumPdivisors(36)   
