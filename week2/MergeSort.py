def sort(l,r,A):
    nl,nr=len(l),len(r)
    i=j=k=0
    while i<nl and j<nr:
        if l[i]<r[j]:
            A[k]=l[i]
            i+=1
            k+=1
        else:
            A[k]=r[j]
            j+=1
            k+=1
    while i<nl:
        A[k]=l[i]
        i+=1
        k+=1
    while j<nr:
        A[k]=r[j]
        j+=1
        k+=1

def mergesort(A):
    n=len(A)
    l=[]
    r=[]
    if n<2:
        return n
    mid=n//2
    for i in range(0,mid):
        l.append(A[i])
    for j in range(mid,n):
        r.append(A[j])
    mergesort(l)
    mergesort(r)
    sort(l,r,A)

A=[9,12,3,19,11,5,21,15,10]
print('Before sorting-',A)
mergesort(A)
print('After sorting-',A)
