def parse_riverLog(fl):
    d = {}
    for line in fl:
        lst = []
        lst = line.rstrip().split("|", 3)
        if lst[0] in d.keys():
            d[lst[0]].append(lst[1:4])
        else:
            d[lst[0]] = lst[1:4]

    print "Total revenue by customer:"
    for k,v in d.items():
        sum = 0
        s = str(k) + " - $"
        for val in v:
            if "." in val:
                sum = sum + float(val)
            elif type(val) == list:
                sum = sum + float(val[2])
            else:
                continue

        s = s + str(sum)
        print s

    print "Purchase by Pedro:"
    for k,v in d.items():
        sum = 0
        if k == 'Pedro':
            for val in v:
                if type(val) == list:
                    s = val[0] + " - $" + val[2]
                    print s
                elif val == "groceries" or val == "tobacco" or val == "fuel":
                    s = val + " - $"
                elif "." in val:
                    s = s + val
                    print s
                else:
                    continue    


fl = open("/Users/Nikhil/Documents/top.txt", "r")
parse_riverLog(fl)
