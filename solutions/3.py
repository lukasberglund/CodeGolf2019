def ls(s):
    b = 0
    m = 0
    for i in range(1, len(s)):
        if s[i] < s[i-1]:
            if i - b > m:
                m = i - b
                mb = b
                me = i
            b = i
    if len(s) - b > m:
        mb = b
        me = len(s) - 1
    return s[mb : me]

f = open("../inputs/3").read()
print(f)
