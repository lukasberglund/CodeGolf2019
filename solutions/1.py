def p(n):
    for j in range(2, n):
        if n % j == 0:
            return False
    return True
for i in range(3, 10000):
    if p(i) and p(i + 2):
        print("%s %s" %(i, i + 2))
