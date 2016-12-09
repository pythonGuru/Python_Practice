# Nikhil Tyagi
# Function returns all strings from list that constitute original given string

def word_split(s,l):
    #if output is None:
    #        output = []
    new_lst = []
    len_new = 0
    #if len(l) == 0:
    for elem in l:
        if elem in s:
            new_lst.append(elem)
            len_new = len_new + len(elem)
        else:
            continue

    if len_new == len(s):
        return new_lst
    else:
        return []

# Test Run
print word_split('themanran', ['clown','man','ran'])
