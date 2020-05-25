class arrangement:
    def permutation(n1,r1):
        p_counter1=0
        count1=n1-r1
        for p_counter2 in range(count1+1,n1+1):
            if p_counter1==0:
                p_counter1=p_counter2+p_counter1
            elif p_counter1!=0: 
                p_counter1=p_counter2*p_counter1       
        print('The number of possible combination of {} objects from a set on {} objects is {}' .format(r1,n1,p_counter1))
    def combination(n2,r2):
        C_counter1=0
        count2=n2-r2
        for C_counter2 in range(count2+1,n2+1):
            if C_counter1==0:
                C_counter1=C_counter2+C_counter1
            elif C_counter1!=0: 
                C_counter1=C_counter2*C_counter1                
        C_counter1=C_counter1/r2        
        print('The number of possible combination of {} objects from a set on {} objects is {}' .format(r2,n2,C_counter1))
        
        
               
arrangement.permutation(5,2)
arrangement.combination(6,2)

#permutation_combination