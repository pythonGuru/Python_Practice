def finder(l1, l2):

    result = 0

    for num in l1+l2:
        result^=num
        print result

    return result    

print finder([5,5,7,7], [5,7,7])
