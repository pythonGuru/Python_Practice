def reduced_string():

    s = raw_input("")
    n = len(s)

    str = ""
    count = 0

    i = 0
    for i in range(n):
        if count == 1 or count%2 != 0:
            str = str + s[i]
            count = 0
        else:
            j = i
            while j<n:
                if s[i] == s[j]:
                    count += 1
                    j += 1
                else:
                    break



    if str == "":
        print "Empty String"
    else:
        print str

reduced_string()
