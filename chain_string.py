def chain_string(arr):
    d = {}
    for elem in arr:
        l = len(elem)
        if d[elem[0]] in d:
            d[elem[0]] += 1
        else:
            d[elem[0]] = 1
        if d[elem[l]] in d:
            d[elem[l]] += 1
        else:
            d[elem[l]] = 1

    for elem in d:
        if d[elem] == 2:
            continue
        else:
            return False

    return True

print chain_string(["geek", "king"])
