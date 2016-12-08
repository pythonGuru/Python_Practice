def chars_inString(s):
    p = ""
    count = 0

    for i in range(len(s)):

        if s[i] == " ":
            p = p + str(count) + " "
            count = 0
        elif i == len(s) - 1:
            count = count + 1
            p = p + str(count)
        else:
            count = count + 1

    print p

chars_inString("This is a short sentence.")
#Output: Needs to be "4 2 1 5 9"
