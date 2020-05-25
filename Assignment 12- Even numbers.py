# assignment 12

evenlist=[]
def filter1(i):
    value2=i%2
    if value2==0:
        evenlist.append(i)

list2=[2,3,5,6,8,9,10,11,13,16]
for i in list2:
    filter1(i)
print('The Even numbers in the list are {}'.format(evenlist))  