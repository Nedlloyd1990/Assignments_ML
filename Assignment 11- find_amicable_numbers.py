# assignment 11

amicable_numbers=[]

def find_amicable_numbers(range1):
    count=0
    count1=0
    for value in range(1,range1):
        for i in range(1,value):
            i1=value%i
            if i1==0:
                count=count+i

        for i2 in range(1,count):
            i3=count%i2
            if i3==0:
                count1=count1+i2
        
        if value==count1 and value!=count:
            amicable_numbers.append('{},{}'.format(count,count1))
        count=0
        count1=0

    print('amicable_numbers within range {} is {}'.format(range1,amicable_numbers))
    
find_amicable_numbers(10000)    