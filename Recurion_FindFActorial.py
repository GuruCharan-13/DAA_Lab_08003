# using tail call optimization

def fact(n,carry):
    if n==0 or n==1:
        return carry
    return fact(n-1,carry*n)

num=int(input('enter a number: '))
print('fact({})={}'.format(num,fact(num,1)))
