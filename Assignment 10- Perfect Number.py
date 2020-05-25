collect=[]
perfect_no=[]
value=1000
for loop in range(value):
    for i in range(1,loop):
        i1=loop%i
        if i1==0:
            collect.append(i)
    sum_all=sum(collect)
    collect.clear()
    if sum_all==loop:
        perfect_no.append(sum_all)
        
print(perfect_no)

