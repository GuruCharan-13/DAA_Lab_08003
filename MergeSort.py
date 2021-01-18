#  merge sort
def merge(arr,lo,mid,hi):
    left,right = arr[lo:mid+1] ,arr[mid+1:hi+1]
    n,m=len(left),len(right)
    i=j=0
    k=lo
    
    while (i<n) and (j<m):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1 
        else:
            arr[k]=right[j]
            j+=1 
        k+=1 
        
    while i<n:
        arr[k]=left[i]
        i+=1 
        k+=1 
        
    while j<m:
        arr[k]=right[j]
        j+=1 
        k+=1 
    
def ms(arr,lo,hi):
    if lo>=hi:return
    mid=(lo+hi)//2
    ms(arr,lo,mid)
    ms(arr,mid+1,hi)
    merge(arr,lo,mid,hi)



arr=[int(i) for i in input('enter the elements of the array').split()]
ms(arr,0,len(arr)-1)
print(arr)
