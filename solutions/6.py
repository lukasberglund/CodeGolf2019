# print(len("                         "))
p = " "
s = "*"
def arrow(i):

    prunt(p*i+s*3+p*53+s*3)
    i+=2
    prunt(p * i + s * 5 + p * 45 + s * 2 + p * 2 + s*3)
    i+=3
    prunt(p * i + s * 7 + p * 33 + s * 7 + p * 3 + s*2)
    i+=4
    prunt(p * i + s * 14 + p * 12 + s * 13 + p * 6 + s * 2)
    i+=4
    prunt(p * i + s * 30 + p * 10 + s)
    i+=7
    prunt(p * i + s * 16)

def pi(s, n):
    p(" " * n + s)

def prunt(s):
    print(s)

def g(l):
    r = ""
    for n in range(len(l)):
        if n % 2 == 0:
            r += " " * l[n]
        else:
            r += "*" * l[n]
    return r
def h(s, l):
    pass
def e():
    print()
prunt(p * (47+5) + s * 9)

arrow(5)
e()
e()
prunt(p * (47+12) + s * 9)

arrow(15)
e()
e()
prunt(p * (47+25) + s * 9)

arrow(25)
