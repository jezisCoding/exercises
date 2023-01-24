# diagonala C like
def diagonala_c1(m):
    i = 0
    res = 1
    for x in m:
        res = res * x[i]
        i += 1
    return res

def diagonala_c2(m):
    i = len(m[0])-1
    res = 1
    for x in m:
        res = res * x[i]
        i -= 1
    return res

# diagonala pythonic
def diagonala_p1(m):
    res = 1
    for i in range(len(m)):
        res = res * m[i][i]
    return res

def diagonala_p2(m):
    res = 1
    for i in range(len(m)):
        res = res * m[i][len(m[0])-1-i]
    return res

matica = [[1,2], 
          [3,4]]

print(diagonala_p1(matica))
print(diagonala_p2(matica))

