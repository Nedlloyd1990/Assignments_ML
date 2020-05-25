#Point=1000
not_prime_no=[]
prime_no=[]
twin_prime=[]

class twin_prime_gr:
    def __init__(self,Point):
        for i in range(1,Point):
            for i1 in range(1 , Point):
                if i==i1 or i1==1:
                    continue
                elif i1!=i1 or i1!=1:   
                    output=i%i1
                    if output==0:
                        if i not in not_prime_no:                
                            not_prime_no.append(i)
                            
    def prime_numbers(Point):   
        for count1 in range(1, Point):
            if count1 not in not_prime_no:
                prime_no.append(count1)
    def find_twin_primes(Point):             
        length=len(prime_no)                    
        for counter in range(1,length):
            diff=prime_no[counter]-prime_no[counter-1]
            if diff==2:
                twin_prime.append('{},{}'.format(prime_no[counter-1],prime_no[counter])) 

range1=1000     # enter the limit here. current limit is 1000   

twin_prime_gr(range1)
twin_prime_gr.prime_numbers(range1)
twin_prime_gr.find_twin_primes(range1)
#print(not_prime_no)
#print(prime_no)
print(" Twin Prime numbers less than {} are {}".format(Point,twin_prime))
 