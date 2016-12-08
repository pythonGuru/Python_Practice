def finder(l1, l2):

    d = {}

    for item in l1:
        if item in d.keys():
            d[item] += 1
        else:
            d[item] = 1

    for item in l2:
        if item in d.keys():
            d[item] -= 1
        else:
            d[item] = 1

    for item in d:
        if d[item] != 0:
            return item

print finder([5,5,7,7], [5,7,7])
