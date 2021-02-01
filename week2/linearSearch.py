# Linear search

arr=[int(i) for i in input().split()]
k=int(input('enter the element you want to find  '))

inds=[]

for ind,ele in enumerate(arr):
    if ele==k:
        inds.append(ind)
        
if inds:
    print('the element is found at the indices: ',*inds)
else:
    print('the element is not found')
