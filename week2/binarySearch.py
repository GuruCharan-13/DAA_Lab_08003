# binary search

arr=[int(i) for i in input().split()]
arr.sort()
k=int(input('enter the element you want to find  '))

inds=[]

def binsrc(arr,key,lo,hi):
    if lo<hi:
        mid=lo+(hi-lo)//2
        if arr[mid]==key:
            return (True,mid)
        elif arr[mid]>key:
            binsrc(arr,key,mid+1,hi)
        else:
            binsrc(arr,key,lo,mid)
    return (False,-1)
re=binsrc(arr,k,0,len(arr)-1)
if re[0]:
    print('the element is found at the index ',re[1])
else:
    print('the element is not found')
