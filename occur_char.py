def occur_char(phrase):
    d = {}
    s = ""

    for elem in phrase:
        if elem in d:
            d[elem] += 1
        else:
            d[elem] = 1

    for elem in phrase:
        while d[elem] != 0:
            s = s + elem
            d[elem] = d[elem] - 1
    return s


print   occur_char("geeksforgeeks")
