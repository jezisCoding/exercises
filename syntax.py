a, b, c = 1, 2, "styri"
print(a, b, c)

d = e = "pet"
print(d, e)

def fibo(n):
    a = b = 1
    for i in range(n):
        nxt = a + b
        a = b
        b = nxt

    return nxt
