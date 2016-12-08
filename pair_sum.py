def pair_sum(l,s):

    new_list = []
    #lnt = len(l)
    d = {}

    for item in l:
        if item in d.keys():
            d[item] += 1
        else:
            d[item] = 1

    for item in d.keys():
        if (s - item) in d:
            new_list.append((item,(s-item)))
            del d[item]

    return len(new_list)

print pair_sum([1,9,2,3,8,7,4,6,5,5,13,14,11,13,-1],10)
