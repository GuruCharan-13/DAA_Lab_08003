def TOH(n,src,dest,hlpr):
    if n==0:return
    TOH(n-1,src,hlpr,dest)
    print('move disc',n,'from',src,'to',dest)
    TOH(n-1,dest,hlpr,src)

TOH(4,'a','b','c')
