def funk(a, b, c):
    print(a, b, c)

def funky(*args, **kwargs):
    print(args)
    print(*args)
    print()
    print(kwargs)
    print(*kwargs)
    #print(**kwargs)

#funk('qwe', 'asd', 'zxc')

funky('qwe', b='asd', c='zxc')

