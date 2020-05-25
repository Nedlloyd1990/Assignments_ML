prime_factors=[]

def find_prime_factor(Value):
    for counter in range(1000):
        for x2 in range(2,1000):
            z=Value%x2
            if z!=0:
                continue
            elif z==0:
                Value=Value/x2
                prime_factors.append(x2)
                break

find_prime_factor(56)
print('the prime factor  is {}'.format(prime_factors))