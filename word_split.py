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

    return new_lst

print word_split('ilovedogsjohn', ['i','am','a','dogs','lover','love','john'])
