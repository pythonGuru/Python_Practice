
def anag(s, q):

    s1 = s.replace(" ","")
    q1 = q.replace(" ","")

    if len(s1) != len(q1):
        return False

    a1 = s1.lower()
    a2 = q1.lower()

    d1 = {}

    for i in a1:
        if i in d1.keys():
            d1[i] += 1
        else:
            d1[i] = 1

    for j in a2:
        if j in d1.keys():
            d1[j] -= 1
        else:
            d1[j] = 1

    for k in d1.keys():
        if d1[k] != 0:
            return False
        return True

print anag("abc", "cba")
