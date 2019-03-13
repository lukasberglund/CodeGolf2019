def p(word):
    for i in range(len(word), 0, -1):
        print(word[:i])
    for i in range(2, len(word) + 1):
        print(word[:i])

p("java")
