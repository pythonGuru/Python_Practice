def unique_subStr(arr, str):

    d = {}

    lnth = 0
    min_len = len(str)
    uniq = ""

    #Start traversing string
    #while min_val != True:
    for i in range(0,len(str)):
        min_str = ""
        if bool(d) == False:
            for item in arr:
                d[item] = 1

        for j in range(i,len(str)):

            if bool(d) == False:
                lnth = len(min_str)
                if lnth <= min_len:
                    min_len = lnth
                    uniq = min_str
                    break

            #Populate dictionary with unique chars
            if (str[j] in d.keys()) & (bool(d) != False):
                del d[str[j]]
                min_str = min_str + str[j]
            else:
                min_str = min_str + str[j]



    return uniq

print unique_subStr("xyza", "xaxyyzzaxaayzz")
