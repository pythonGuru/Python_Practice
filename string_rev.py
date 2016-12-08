def string_rev(str):
    s = ""
    end = len(str)
    start = 0

    for i in range(end-1,start-1,-1):
        if str[i] == " " or i==0:
            s1 = str[i:end]
            s = s + s1
            end = i
    return s

print string_rev("nik is     ")
