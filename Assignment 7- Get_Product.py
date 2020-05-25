
def get_product(x): 
    product=1
    for i in str(x):
        product=product*int(i)
    print('the product of {} is {}'.format(x,product))

get_product(23)    