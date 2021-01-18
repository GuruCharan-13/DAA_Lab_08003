def find_Min_Max(arr,mi,ma):
    if arr==[]:
        return (mi,ma)
    ele=arr.pop()
    if ele<mi:  mi=ele
    if ele>ma:  ma=ele
    return find_Min_Max(arr,mi,ma)
mi,ma=find_Min_Max([1,3,4,2,6,5],float('inf'),-float('inf'))
print('the minimum is',mi)
print('the maximum is',ma)
